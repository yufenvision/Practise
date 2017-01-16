package onLine;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.firefox.FirefoxDriver;

public class TestDemo1 {
	public static void main(String[] args){
		System.setProperty("webdriver.firefox.bin", "D:/Program Files (x86)/Mozilla Firefox/firefox.exe");
		System.out.println("loadFirefoxSuccessfully!");
		System.setProperty("webdriver.geko.driver","D:/Drivers/geckodriver.exe");
		System.out.println("loadGeckodriverSuccessfully!");
		WebDriver driver= new FirefoxDriver();
		driver.get("http://student.uestcedu.com/console/main.html");
		WebElement searchBox=driver.findElement(By.id("item_logout"));
		searchBox.click();
		delay(2);
		driver.switchTo().alert().accept();
		delay(2);
		driver.findElement(By.id("txtLoginName")).clear();
		driver.findElement(By.id("txtLoginName")).sendKeys("20160210447670");
		driver.findElement(By.id("txtPassword")).clear();
		driver.findElement(By.id("txtPassword")).sendKeys("2192168");		
		driver.findElement(By.id("login_button")).click();
		delay(2);
	    	driver.findElement(By.linkText("在线课程")).click();
//	    	delay(5);
//	    	driver.findElement(By.xpath("/html/body/table[1]/tbody/tr/td/div/a[1]/div[2]")).click();
	    	delay(7);
	    	try{
	    	WebDriver temDriver=driver.switchTo().frame("f_M00370003");
	    	temDriver.findElement(By.xpath("//*[@id='tr_tblDataList_6']/td[8]/a[1]")).click();
	    	
/*	    	WebElement ele=null;//通过查看是否完全抓取不到该页面此内容，还是应为浏览器刷新的缘故
	    	while(ele==null){
	    		try {
	    			ele= driver.findElement(By.xpath("//*[@id='tr_tblDataList_6']/td[8]/a[1]"));
				} catch (Exception e) {
					continue;
				}
	    	}
	    	ele.click();*/
	    	}catch(Exception e){
	    	e.printStackTrace();
	    	}
	    	String [] handles=new String[driver.getWindowHandles().size()];
	    	System.out.println(handles.length);
	   	driver.getWindowHandles().toArray(handles);
	    	driver.switchTo().window(handles[1]);
//	   	driver.switchTo().frame("w_top");
	    	driver.switchTo().frame("w_main");
//	    	driver.switchTo().frame("w_exam_quit");
	    
	    	delay(2);
	    	driver.findElement(By.id("spanLearnContent_71266")).click();
	    	driver.switchTo().defaultContent();//切入frame的时候，如果需要切入同级frame或上级frame，需先切换到初始状态defaultContent()
	    	driver.switchTo().frame("w_main");
	    	driver.switchTo().frame("w_code");
	    	for(int i=0;i<122;i++){
	    	try{
	    		Thread.sleep(2000);
	    		driver.findElement(By.id("btnNext")).click();
	    		Thread.sleep(70000);	
	    	}catch(InterruptedException e){
	    		e.printStackTrace();
	    	}
	    	}
		driver.quit();
		System.out.println("Execution successfully");
		}
	public static void delay(int i){
		try{
			Thread.sleep(i*1000);
		}catch(InterruptedException e){
			e.printStackTrace();
		}
	}
}
