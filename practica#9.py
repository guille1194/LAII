oo000 = [ [ 'admin' , '123' , 'Administrador' ] ]
ii = [ ]
if 51 - 51: IiI1i11I
#metodos con init
class Iii1I1 :
 def __init__ ( self , nombreu , clave , rol ) :
  self . nombreu = nombreu
  self . clave = clave
  self . rol = rol
  if 73 - 73: II1I1iiiiii * ooo0OO / o0OO00 / oo
class i1iII1IiiIiI1 :
 def __init__ ( self , nombree , horas_trabajo , sueldo_hora ) :
  self . nombree = nombree
  self . horas_trabajo = horas_trabajo
  self . sueldo_hora = sueldo_hora
  if 40 - 40: ooOoO0O00 * IIiIiII11i
def o0oOOo0O0Ooo ( nombreu , clave ) :
 for I1ii11iIi11i in oo000 :
  if I1ii11iIi11i [ 0 ] == nombreu :
   if I1ii11iIi11i [ 1 ] == clave :
    return True
    if 48 - 48: oO0o / OOooOOo / I11i / Ii1I
def IiiIII111iI ( ) :
 print 30 * "-" , "MENU" , 30 * "-"
 print "1. Calcular nomina"
 print "2. Registrar Empleados"
 print "3. Desplegar Empleados"
 print "4. Salir"
 print 67 * "-"
 if 34 - 34: iii1I1I / O00oOoOoO0o0O . O0oo0OO0 + Oo0ooO0oo0oO . I1i1iI1i - II
def Oo ( ) :
 I1Ii11I1Ii1i = 0
 Ooo = 0
 print 67 * "-"
 for o0oOoO00o in ii :
  if o0oOoO00o . horas_trabajo > 0 :
   i1 = o0oOoO00o . horas_trabajo - 30
   oOOoo00O0O = ( o0oOoO00o . sueldo_hora * 30 ) + ( i1 * ( o0oOoO00o . sueldo_hora * 1.03 ) )
   I1Ii11I1Ii1i += oOOoo00O0O
   Ooo += i1
   print "Empleado: " + o0oOoO00o . nombree + ", " + "Horas Trabajadas: " + str ( o0oOoO00o . horas_trabajo ) + ", " + "Horas Extra: " + str ( i1 ) + ", " + "Sueldo Total: " + str ( oOOoo00O0O )
 print 67 * "-"
 print "Resumen"
 print "Nomina Total: " + str ( I1Ii11I1Ii1i )
 print "Total de Horas Extra en Horas: " + str ( Ooo )
 print
 print
 if 15 - 15: I11iii11IIi
def O00o0o0000o0o ( ) :
 print
 print "Ingrese los sigientes datos"
 print
 O0Oo = raw_input ( "Nombre Empleado: " )
 ooIiII1I1i1i1ii = input ( "Horas Trabajadas: " )
 IIIII = 28
 ii . append ( i1iII1IiiIiI1 ( O0Oo , ooIiII1I1i1i1ii , IIIII ) )
 print "Exito"
 print
 if 26 - 26: O00OoOoo00 . iiiI11 / O00oOoOoO0o0O * Ii1I / IiI1i11I
def iIIIiI11 ( ) :
 iII111ii = 1
 for o0oOoO00o in ii :
  print str ( iII111ii ) + ".- " + o0oOoO00o . nombree + ", " + "Horas Trabajadas: " + str ( o0oOoO00o . horas_trabajo )
  + + iII111ii
  if 3 - 3: II + II1I1iiiiii
I1Ii = { '1' : Oo , '2' : O00o0o0000o0o , '3' : iIIIiI11 }
if 66 - 66: I1i1iI1i
print 67 * "-"
print "Bienvenido al Sistema"
print 67 * "-"
print
print "Inicie Sesion para acceder al sistema"
oo0Ooo0 = raw_input ( "Nombre Usuario: " )
I1I11I1I1I = raw_input ( "Contrasenia: " )
if 90 - 90: ooOoO0O00 + O00oOoOoO0o0O / Ii1I % ooOoO0O00 - II1I1iiiiii
if o0oOOo0O0Ooo ( oo0Ooo0 , I1I11I1I1I ) :
 iIii1 = True
 while iIii1 :
  IiiIII111iI ( )
  oOOoO0 = raw_input ( "Escoger opcion: " )
  print
  if oOOoO0 == 4 :
   print "Hasta luego"
   iIii1 = False
  else :
   I1Ii [ oOOoO0 ] ( )
   print
else :
 print "Error al iniciar sesion"
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
