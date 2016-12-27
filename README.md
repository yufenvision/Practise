# Practise
package login;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.firefox.FirefoxDriver;

public class Zhbgglxt {
	public static void main(String [] agrs){
		//如果启动出现问题，可以使用System.setProperty指出firefox.exe的路径
		System.setProperty("webdriver.firefox.bin", "D:/Program Files (x86)/Mozilla Firefox/firefox.exe");
		System.setProperty("webdriver.geko.driver","D:/Drivers/geckodriver.exe");
		WebDriver driver=new FirefoxDriver();
		String url=("http://172.22.200.198/default/abframe/auth/login.jsp?retCode=");
		driver.get(url);
		delay(2);
		WebElement denglu =driver.findElement(By.id("userName"));
		denglu.sendKeys("qiuyi");
		WebElement mima = driver.findElement(By.id("password"));
		mima.sendKeys("000000");
		driver.findElement(By.id("login")).click();
		delay(5);
		boolean sf;
		
		driver.quit();
	}
	
	public static void delay(int i){
		try{
			Thread.sleep(i*1000);
		}catch(InterruptedException e){
			e.printStackTrace();
		}
	}
}
