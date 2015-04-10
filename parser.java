import java.util.*;
import java.io.*;
public class parser
{
	public static void main(String[] args)
	{
		System.out.println("here");
		String line, filename = "/home/aaron/Programing/CSI531/Project/tweets", delims = " ,.?!#&();:", word;
		int hot = 0, cold = 0, rainy = 0, snowy = 0, humid = 0, freezing = 0, sunny = 0, windy = 0, cloudy = 0, sleet = 0, ice = 0;
		File file = new File("/home/aaron/Programing/CSI531/Project/tweets/la_totals.txt");
		file.createNewFile();
		PrintWriter writer =  new PrintWriter("/home/aaron/Programing/CSI531/Project/tweets/la_totals.txt");
		try
		{
			BufferedReader reader = new BufferedReader(new FileReader(filename));
			while ((line = reader.readLine()) != null)
			{
				StringTokenizer st = new StringTokenizer(line, delims);
				while (st.hasMoreElements())
				{
					word = st.nextToken();
					if (word.equals("hot"))
					{
						hot++;
					}
					else if (word.equals("cold"))
					{
						cold++;
					}
					else if (word.equals("rainy") || word.equals("raining"))
					{
						rainy++;
					}
					else if (word.equals("snowy") || word.equals("snowing"))
					{
						snowy++;
					}
					else if (word.equals("humid"))
					{
						humid++;
					}
					else if (word.equals("freezing") || word.equals("bitter"))
					{
						freezing++;
					}
					else if (word.equals("sunny"))
					{
						sunny++;
					}
					else if (word.equals("windy") || word.equals("breezy"))
					{
						windy++;
					}
					else if (word.equals("cloudy"))
					{
						cloudy++;
					}
					else if (word.equals("sleet") || word.equals("sleeting"))
					{
						sleet++;
					}
					else if (word.equals("ice") || word.equals("icy"))
					{
						ice++;
					}
				}
			}
			reader.close();
		}
		catch (Exception e)
		{
			System.err.format("Exception occured trying to read '%s'.", filename);
			e.printStackTrace();
			//System.exit(0);
		}
		writer.write("hot,%d" + String.valueOf(hot));
		writer.write("cold,%d" + String.valueOf(cold));
		writer.write("rainy,%d" + String.valueOf(rainy));
		writer.write("snowy,%d" + String.valueOf(snowy));
		writer.write("humid,%d" + String.valueOf(humid));
		writer.write("freezing,%d" + String.valueOf(freezing));
		writer.write("sunny,%d" + String.valueOf(sunny));
		writer.write("windy,%d" + String.valueOf(windy));
		writer.write("cloudy,%d" + String.valueOf(cloudy));
		writer.write("sleet,%d" + String.valueOf(sleet));
		writer.write("ice,%d" + String.valueOf(ice));
		writer.close();
	}
}
