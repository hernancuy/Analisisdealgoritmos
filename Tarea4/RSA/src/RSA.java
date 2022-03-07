/* Task 4 
Analisis de algoritmos 2022

Algoritmo principal RSA tomado de Algorithms Unlocked, Cormen 2013
Jorge Duitama


Hernan David Cuy
Carlos Torres

*/
import java.math.BigInteger;
import java.util.Scanner;
import java.time.Duration;
import java.time.Instant;

public class RSA {
    
    
    /*multiplicate Inverse  */
    static int modInverse(int a, int m)
    {
	for (int x = 1; x < m; x++)
            if (((a%m) * (x%m)) % m == 1)
                {
                return x;
                }
        return 1;
    } 
    
    /*calculate P(x) and S(x), x is the value to encrypt, y and z params from P(x) and S(x)*/
    static BigInteger calculator(BigInteger x, int y, BigInteger z){
        BigInteger result = x.pow(y);
        return result.mod(z);
    }
    
    static int gcd(int e, int r)
    {
        if (e == 0)
            return r;
        else
            return gcd(r % e, e);
    }
    /*Main*/
    public static void main(String[] args) {
        System.out.println("Tarea 4");
        Scanner scanner = new Scanner(System.in);
        System.out.println( "Digite el numero de bits, el rango va de 3 a 1024:" );
        int bitsize = scanner.nextInt();
        Instant start = Instant.now();
        BigInteger p = MillerRabin.generator(bitsize);
        BigInteger q = MillerRabin.generator(bitsize);
        Instant finish = Instant.now();
        long timeElapsed = Duration.between(start, finish).toMillis();
        System.out.println("Tiempo generacion p y q: " + timeElapsed + "ms");
        BigInteger n = p.multiply(q);
        System.out.println("p = "+p+".");
        System.out.println("q = "+q+".");
        System.out.println("p*q = n = "+n+".");
        BigInteger one = BigInteger.valueOf(1);
        BigInteger p1 = p.subtract(one);
        BigInteger q1 = q.subtract(one);
        BigInteger r = p1.multiply(q1);
        System.out.println("r = "+r+".");
        int e;
        for(e = 2; e < r.intValue(); e++) 
        {
            if (gcd(e, r.intValue()) == 1) {
                break;
            }
        }
        System.out.println("e = "+e+".");
        int d = modInverse(e, r.intValue());
        System.out.println("d = "+d+".");
        System.out.println("RSA llave publica P ("+e+","+n+")");
        System.out.println("RSA llave privada S ("+d+","+n+")");
        Scanner scanner2 = new Scanner(System.in);
        System.out.println("Digite el valor al que desea generar la llave (X)" );
        BigInteger valor = scanner2.nextBigInteger();
        BigInteger px;
        BigInteger ps;
        Instant start2 = Instant.now();
        px = calculator(valor, e, n);
        Instant finish2 = Instant.now();
        long timeElapsed2 = Duration.between(start2, finish2).toMillis();
        System.out.println("Tiempo Generacion P(X) " + timeElapsed2 + "ms");
        BigInteger y = px;
        Instant start3 = Instant.now();
        ps = calculator(y, d, n);
        Instant finish3 = Instant.now();
        long timeElapsed3 = Duration.between(start3, finish3).toMillis();
        System.out.println("Tiempo Generacion Q(X): " + timeElapsed3 + "ms");
        System.out.println("Al encriptar P(x)= "+px+".");
        System.out.println("Al desencriptar S(x)= "+ps+".");
    }
    
}
