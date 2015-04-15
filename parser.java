import java.util.*;
import java.io.*;
public class parser
{
	public static void main(String[] args)
	{
		String line, delims = " ,.?!#&();:", word;
		int hot = 0, cold = 0, rainy = 0, snowy = 0, humid = 0, freezing = 0, sunny = 0, windy = 0, cloudy = 0, sleet = 0, ice = 0;
		File directory = new File("tweet_data");
		if (!directory.exists())
		{
			directory.mkdir();
		}
		File outfile = new File("tweet_data/antalya.data");
		File infile = new File("tweets/antalya_tweets.txt");
		try
		{
			outfile.createNewFile();
		}
		catch (IOException e)
		{
			System.err.format("Exception occured trying to create '%s'.", infile);
			e.printStackTrace();
		}
		try
		{
			BufferedReader reader = new BufferedReader(new FileReader(infile));
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
			System.err.format("Exception occured trying to read '%s'.", infile);
			e.printStackTrace();
			//System.exit(0);
		}
		try
		{
			PrintWriter writer =  new PrintWriter(outfile);
			writer.write("hot," + String.valueOf(hot) + "\n");
			writer.write("cold," + String.valueOf(cold) + "\n");
			writer.write("rainy," + String.valueOf(rainy) + "\n");
			writer.write("snowy," + String.valueOf(snowy) + "\n");
			writer.write("humid," + String.valueOf(humid) + "\n");
			writer.write("freezing," + String.valueOf(freezing) + "\n");
			writer.write("sunny," + String.valueOf(sunny) + "\n");
			writer.write("windy," + String.valueOf(windy) + "\n");
			writer.write("cloudy," + String.valueOf(cloudy) + "\n");
			writer.write("sleet," + String.valueOf(sleet) + "\n");
			writer.write("ice," + String.valueOf(ice) + "\n");
			writer.close();
		}
		catch (FileNotFoundException e)
		{
			System.err.format("Exception occured trying to open '%s'.", infile);
			e.printStackTrace();
		}
	}
}
