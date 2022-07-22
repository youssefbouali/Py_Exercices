class Etudiant ( Personne ) :
	def __init__( self , a , b , number ) :
		Personne.__init__( self, a , b )
		self.num=number
	def afficher ( self ) :
		Personne.afficher ( self )
		print ( 'Num: '+str ( self.num) )
	def modifier_num ( self, number ) :
		self.num=number
	def retourner_num ( self ) :
		return ( self.num)


class Enseignant ( Personne ) :
	def __init__( self , a , b , mat ) :
		Personne.__init__( self , a , b )
		self.matiere=mat
	def afficher ( self ) :
		Personne.afficher ( self )
		print ( ' Matiere : ' , self.matiere )
	def modifier_mat ( self , mat ) :
		self.matiere=mat
	def retourner_mat ( self ) :
		return ( self.matiere )
