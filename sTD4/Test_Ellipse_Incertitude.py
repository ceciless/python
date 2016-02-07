# -*-coding:Latin-1 -*
# etude d'ellipse d'incertitude
import scipy as sc              # pour la manipulation de fonctions de maths
import numpy as np              # pour la manipulation de matrice
import pylab as pl              # pour la manipulation graphique
from matplotlib.patches import Ellipse # pour la manipulation des ellipses

# Methode permettant de generer des points aléatoires en deux dimension selon 
# une distribution normale
def GeneratePoints(N=10,mean=(0,0),cov=[[1,0],[0,1]]):
    """ Generation de points aléatoires
        N : nbre de points pour le nuage
        mean : coord moyenne (x,y) du nuage de points (le centre)
        cov : Matrice de covaraince (une liste : cov[0][1]=0)
    """
    
    # Definition des points via une loi normale
    # retourne un numpy.ndarray [[x0 y0]...[xn yn]]
    points  =np.random.multivariate_normal(mean, cov, N)
    #points2 = points.T #ou .transpose()
    
    mean_bar = [np.mean(points[:,0]), np.mean(points[:,1])] # estime le centre
    cov_bar  = np.cov(points.transpose())   # estime matrice de covariance
 
    # Affichage 
    print " Nombre de points: ", N
    print " Moyenne estimée: ", mean_bar
    print " Matrice de covariance estimée: "
    print cov_bar
    
    return (points, mean_bar, cov_bar)

# Affichage de la distribution
def AfficheDistribution(points, center):
    """ Affichage des points de la distribution """
    x = points[:,0] # extraction coordonnées x de type < type 'numpy.ndarray' >    
    y = points[:,1] # idem mais pour y
    
    pl.figure()
    #pl.plot(x,y,'o',label="points")                   # affichage avec un plot
    pl.scatter(x,y, c='r', marker='o', label="Points") # affichage avec scatter
    pl.plot(center[0],center[1], 'db', label="Centre") # affichage du centre
    pl.xlabel("x")
    pl.ylabel("y")
    pl.title("Distribution gaussienne 2D")
    pl.legend()
    pl.axis("equal")
    pl.show()    
    
# Methode permettant d'estimer l'ellipse d'incertitude en fonction de e
def EllipseIncertitude(covar, e=2.146):
    """ Ellipse d'incertitude 
        covar: Matrice de covariance (numpy.array)
        e    : facteur d'echelle, si plusieurs valeurs alors numpy.array
    """
    
    # Estimation de l'orientation du grand axe
    # cf wikipedia à propos de arctan2 (atan2)
    phi = 0.5*np.arctan2(2*covar[1,0], covar[0,0]-covar[1,1])
    
    # Estimation de a et b
    lambda1  = np.linalg.eigvals(covar) # Valeurs propres (ou np.linalg.eig pour avoir valeurs et vecteurs propres)
    lambda12 = lambda1**2 
    a = e*np.sqrt(np.max(lambda12))     # Estimation du grand axe
    b = e*np.sqrt(np.min(lambda12))     # Estimation du petit axe
    
    return(phi, a, b)
    
# Methode pour affichage d'ellipse d'incertitude
def AfficheEllipse(points, center, phi, a, b, e):
    """ pour affichage des ellipses d'incertitudes"""    
    x = points[:,0] # extraction coordonnées x de type < type 'numpy.ndarray' >    
    y = points[:,1] # idem mais pour y
    
    fig = pl.figure()           # Creation d'une figure
    ax  = fig.add_subplot(111)  # Creation d'une 'zone' pour l'affichage
    
    # Affichage du nuage de points
    fig_pts = ax.scatter(x, y, c='r', marker='o')
    
    # ici il va y avoir un probleme avec la legende il faut 'bidouiller'
    container = []          # variable permettant de stocker l'ensemble des courbes
    container_label = []    # idem mais pour stocker les labels des courbes
    container.append(fig_pts)
    container_label.append('Point_GPS')
    
    # Partie permettant l'affichage des ellipses d'incertitudes 
    # cf. : http://matplotlib.org/examples/pylab_examples/ellipse_demo.html
    val_center = center
    val_angle = np.rad2deg(phi)
    for k in range(len(e)):
        # Traitement pour une ellipse d'incertitude
        val_a = a[k]
        val_b = b[k]
        # Construction de l'ellipse
        fig_ell = Ellipse(xy=val_center, width=val_a, height=val_b, angle=val_angle)
        
        fig_ell.set_alpha(0.2)              # Pour la transparence
        fig_ell.set_facecolor(pl.rand(3))   # Pour la couleur de l'ellipse (aleatoire)
        ax.add_artist(fig_ell)              # Affichage de l'ellipse
    
        container.append(fig_ell)           # Stockage dans le container
        container_label.append("E: "+str(e[k]))
        
    # Utilisation du container pour réaliser la légende
    # ax.legend(container, container_label)
    ax.legend(container, ["Point GPS", "99%","95%","90%"])
        
    # finition pour avoir une jolie figure
    pl.xlabel("x")
    pl.ylabel("y")
    pl.title("Distribution Gaussienne 2D")
    pl.show()
        
###############################################################################
# Methode main
if __name__ == "__main__":
    print("Test ellipse d'incertitude")
    
    print(" -> Création des points")
    (data, centre, covariance) = GeneratePoints(1000,(10,12),[[3,1],[1,8]])
    
    print(" -> Affichage des données")
    AfficheDistribution(data, centre)
    
    print(" -> Estimation des ellipses d'incertitude pour 3 valeurs de e")
    E = np.array([3.035, 2.448, 2.146])
    (tab_phi, tab_a, tab_b) = EllipseIncertitude(covariance, E)
    
    # Affichage des points avec ellipses d'incertitude
    AfficheEllipse(data, centre, tab_phi, tab_a, tab_b, E)
    
    print "Fin Test"