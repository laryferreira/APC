a,b,c = list(map(float,input().split()))
triangulo=0.5*a*c
circulo=3.14159*c*c
trapezio=(a+b)/2.0*c
quadrado=b*b
retangulo=a*b
print("TRIANGULO: %.3lf"%triangulo)
print("CIRCULO: %.3f"%circulo)
print("TRAPEZIO: %.3f"%trapezio)
print("QUADRADO: %.3f"%quadrado)
print("RETANGULO: %.3f"%retangulo)
