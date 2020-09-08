# 코로나19 한국 감염통계 CSV추출(시/도별, 일별, 전체 포함)
# COVID19 Korea Infection Statistics to CSV(including city/province, daily and total)

## 코로나19의 한국내 감염 데이터를 CSV형태로 만들어주는 파이썬 스크립트입니다. 목적에 맞도록 대충 짰습니다. 잘 굴러가긴 합니다. Python 3버전용입니다.
## This is small Python script that makes Corona 19's infection data in Korea in CSV format. It's a rough plan for the purpose. It's for Python 3.

### 1. 먼저 공공데이터 포털에 가입하여 하기 API Key를 받아주세요.
### 1. Please sign up for the PublicDataPortal(the Korean government site for public data) and receive the API key below.(site is in Korean)
### https://www.data.go.kr/tcs/dss/selectApiDataDetailView.do?publicDataPk=15043378

### 2. 소스의 11번째줄의 MY API KEY에 받은 키를 넣어주세요
### 2. write your key on the MY API KEY in the 11th row of the source file.

### 3. 실행하면 처음 데이터는 3월 3일부터 현재까지의 데이터를 한번에 받아오기 시작합니다.
### 3. When you run the script, the data will begin to be received at once from March 3rd to the present day.

### 4. 만들어진 covid19kr.txt를 엑셀로 열어서 다듬어서 쓰시면 됩니다.
### 4. Open the covid19kr.txt with excel and enjoy.

공공데이터 포털 매뉴얼을 보시면 아래처럼 다른 데이터도 뽑을 수 있으니. 참고하셔요. 대신 대소문자가 안맞는 경우가 많아서, 하나 대충 호출하셔서 XML파일을 보시고 명확하게 지정하시는 것이 좋습니다.
당장 확진자 누적수인 defCnt가 매뉴얼에는 DEF_CNT로 되어있습니다.

```docx
  resultCode	결과코드	2	1	00	결과코드
  resultMsg	결과메세지	50	1	NORMAL SERVICE	결과메시지
  numOfRows	한 페이지 결과 수	4	1	10	한 페이지당 표출 데이터 수
  pageNo	페이지 수	4	1	1	페이지 수
  totalCount	전체 결과 수	4	1	2	전체 결과 수
  SEQ	게시글번호(국내 시도별 발생현황 고유값)	30	1	1014	게시글번호(국내 시도별 발생현황 고유값)
  CREATE_DT	등록일시분초	30	1	2020-04-10 11:17:34.589	등록일시분초
  DEATH_CNT	사망자 수	15	1	0	사망자 수
  GUBUN	시도명(한글)	30	1	검역	시도명(한글)
  GUBUN_CN	시도명(중국어)	30	1	隔離區	시도명(중국어)
  GUBUN_EN	시도명(영어)	30	1	Lazaretto	시도명(영어)
  INC_DEC	전일대비 증감 수	15	1	4	전일대비 증감 수
  ISOL_CLEAR_CNT	격리 해제 수	15	1	349	격리 해제 수
  QUR_RATE	10만명당 발생률	30	1	-	10만명당 발생률
  STD_DAY	기준일시	30	1	2020년 04월 10일 00시	기준일시
  UPDATE_DT	수정일시분초 	30	1	null	수정일시분초 
  DEF_CNT	확진자 수	15	1	13561	확진자 수
  ISOL_ING_CNT	격리중 환자수	15	1	9	격리중 환자수
  OVER_FLOW_CNT	해외유입 수	15	1	14	해외유입 수
  LOCAL_OCC_CNT	지역발생 수 	15	1	7	지역발생 수 
```
호출 결과 데이터입니다. 참고하세요
```xml
<?xml version="1.0" encoding="utf-8"?>
<response>
	<header>
		<resultCode>00</resultCode>
		<resultMsg>NORMAL SERVICE.</resultMsg>
	</header>
	<body>
		<items>
			<item>
				<createDt>2020-09-06 09:46:13.478</createDt>
				<deathCnt>0</deathCnt>
				<defCnt>1376</defCnt>
				<gubun>검역</gubun>
				<gubunCn>隔離區</gubunCn>
				<gubunEn>Lazaretto</gubunEn>
				<incDec>4</incDec>
				<isolClearCnt>1283</isolClearCnt>
				<isolIngCnt>93</isolIngCnt>
				<localOccCnt>0</localOccCnt>
				<overFlowCnt>4</overFlowCnt>
				<qurRate>-</qurRate>
				<seq>4187</seq>
				<stdDay>2020년 09월 06일 00시</stdDay>
				<updateDt>null</updateDt>
			</item>
			<item>
				<createDt>2020-09-06 09:46:13.478</createDt>
				<deathCnt>0</deathCnt>
				<defCnt>48</defCnt>
				<gubun>제주</gubun>
				<gubunCn>济州</gubunCn>
				<gubunEn>Jeju</gubunEn>
				<incDec>0</incDec>
				<isolClearCnt>27</isolClearCnt>
				<isolIngCnt>21</isolIngCnt>
				<localOccCnt>0</localOccCnt>
				<overFlowCnt>0</overFlowCnt>
				<qurRate>7.16</qurRate>
				<seq>4186</seq>
				<stdDay>2020년 09월 06일 00시</stdDay>
				<updateDt>null</updateDt>
			</item>
			<item>
				<createDt>2020-09-06 09:46:13.478</createDt>
				<deathCnt>0</deathCnt>
				<defCnt>257</defCnt>
				<gubun>경남</gubun>
				<gubunCn>庆南</gubunCn>
				<gubunEn>Gyeongsangnam-do</gubunEn>
				<incDec>6</incDec>
				<isolClearCnt>194</isolClearCnt>
				<isolIngCnt>63</isolIngCnt>
				<localOccCnt>4</localOccCnt>
				<overFlowCnt>2</overFlowCnt>
				<qurRate>7.65</qurRate>
				<seq>4185</seq>
				<stdDay>2020년 09월 06일 00시</stdDay>
				<updateDt>null</updateDt>
			</item>
			<item>
				<createDt>2020-09-06 09:46:13.477</createDt>
				<deathCnt>54</deathCnt>
				<defCnt>1475</defCnt>
				<gubun>경북</gubun>
				<gubunCn>庆北</gubunCn>
				<gubunEn>Gyeongsangbuk-do</gubunEn>
				<incDec>2</incDec>
				<isolClearCnt>1376</isolClearCnt>
				<isolIngCnt>45</isolIngCnt>
				<localOccCnt>2</localOccCnt>
				<overFlowCnt>0</overFlowCnt>
				<qurRate>55.40</qurRate>
				<seq>4184</seq>
				<stdDay>2020년 09월 06일 00시</stdDay>
				<updateDt>null</updateDt>
			</item>
			<item>
				<createDt>2020-09-06 09:46:13.477</createDt>
				<deathCnt>0</deathCnt>
				<defCnt>159</defCnt>
				<gubun>전남</gubun>
				<gubunCn>全南</gubunCn>
				<gubunEn>Jeollanam-do</gubunEn>
				<incDec>3</incDec>
				<isolClearCnt>47</isolClearCnt>
				<isolIngCnt>112</isolIngCnt>
				<localOccCnt>0</localOccCnt>
				<overFlowCnt>3</overFlowCnt>
				<qurRate>8.53</qurRate>
				<seq>4183</seq>
				<stdDay>2020년 09월 06일 00시</stdDay>
				<updateDt>null</updateDt>
			</item>
			<item>
				<createDt>2020-09-06 09:46:13.477</createDt>
				<deathCnt>0</deathCnt>
				<defCnt>90</defCnt>
				<gubun>전북</gubun>
				<gubunCn>全北</gubunCn>
				<gubunEn>Jeollabuk-do</gubunEn>
				<incDec>1</incDec>
				<isolClearCnt>53</isolClearCnt>
				<isolIngCnt>37</isolIngCnt>
				<localOccCnt>1</localOccCnt>
				<overFlowCnt>0</overFlowCnt>
				<qurRate>4.95</qurRate>
				<seq>4182</seq>
				<stdDay>2020년 09월 06일 00시</stdDay>
				<updateDt>null</updateDt>
			</item>
			<item>
				<createDt>2020-09-06 09:46:13.477</createDt>
				<deathCnt>1</deathCnt>
				<defCnt>380</defCnt>
				<gubun>충남</gubun>
				<gubunCn>忠南</gubunCn>
				<gubunEn>Chungcheongnam-do</gubunEn>
				<incDec>2</incDec>
				<isolClearCnt>232</isolClearCnt>
				<isolIngCnt>147</isolIngCnt>
				<localOccCnt>2</localOccCnt>
				<overFlowCnt>0</overFlowCnt>
				<qurRate>17.90</qurRate>
				<seq>4181</seq>
				<stdDay>2020년 09월 06일 00시</stdDay>
				<updateDt>null</updateDt>
			</item>
			<item>
				<createDt>2020-09-06 09:46:13.477</createDt>
				<deathCnt>1</deathCnt>
				<defCnt>141</defCnt>
				<gubun>충북</gubun>
				<gubunCn>忠北</gubunCn>
				<gubunEn>Chungcheongbuk-do</gubunEn>
				<incDec>2</incDec>
				<isolClearCnt>99</isolClearCnt>
				<isolIngCnt>41</isolIngCnt>
				<localOccCnt>2</localOccCnt>
				<overFlowCnt>0</overFlowCnt>
				<qurRate>8.82</qurRate>
				<seq>4180</seq>
				<stdDay>2020년 09월 06일 00시</stdDay>
				<updateDt>null</updateDt>
			</item>
			<item>
				<createDt>2020-09-06 09:46:13.477</createDt>
				<deathCnt>3</deathCnt>
				<defCnt>210</defCnt>
				<gubun>강원</gubun>
				<gubunCn>江原</gubunCn>
				<gubunEn>Gangwon-do</gubunEn>
				<incDec>5</incDec>
				<isolClearCnt>133</isolClearCnt>
				<isolIngCnt>74</isolIngCnt>
				<localOccCnt>5</localOccCnt>
				<overFlowCnt>0</overFlowCnt>
				<qurRate>13.63</qurRate>
				<seq>4179</seq>
				<stdDay>2020년 09월 06일 00시</stdDay>
				<updateDt>null</updateDt>
			</item>
			<item>
				<createDt>2020-09-06 09:46:13.477</createDt>
				<deathCnt>45</deathCnt>
				<defCnt>3625</defCnt>
				<gubun>경기</gubun>
				<gubunCn>京畿</gubunCn>
				<gubunEn>Gyeonggi-do</gubunEn>
				<incDec>47</incDec>
				<isolClearCnt>2359</isolClearCnt>
				<isolIngCnt>1221</isolIngCnt>
				<localOccCnt>45</localOccCnt>
				<overFlowCnt>2</overFlowCnt>
				<qurRate>27.36</qurRate>
				<seq>4178</seq>
				<stdDay>2020년 09월 06일 00시</stdDay>
				<updateDt>null</updateDt>
			</item>
			<item>
				<createDt>2020-09-06 09:46:13.476</createDt>
				<deathCnt>0</deathCnt>
				<defCnt>67</defCnt>
				<gubun>세종</gubun>
				<gubunCn>世宗</gubunCn>
				<gubunEn>Sejong</gubunEn>
				<incDec>0</incDec>
				<isolClearCnt>58</isolClearCnt>
				<isolIngCnt>9</isolIngCnt>
				<localOccCnt>0</localOccCnt>
				<overFlowCnt>0</overFlowCnt>
				<qurRate>19.57</qurRate>
				<seq>4177</seq>
				<stdDay>2020년 09월 06일 00시</stdDay>
				<updateDt>null</updateDt>
			</item>
			<item>
				<createDt>2020-09-06 09:46:13.476</createDt>
				<deathCnt>1</deathCnt>
				<defCnt>113</defCnt>
				<gubun>울산</gubun>
				<gubunCn>蔚山</gubunCn>
				<gubunEn>Ulsan</gubunEn>
				<incDec>1</incDec>
				<isolClearCnt>69</isolClearCnt>
				<isolIngCnt>43</isolIngCnt>
				<localOccCnt>1</localOccCnt>
				<overFlowCnt>0</overFlowCnt>
				<qurRate>9.85</qurRate>
				<seq>4176</seq>
				<stdDay>2020년 09월 06일 00시</stdDay>
				<updateDt>null</updateDt>
			</item>
			<item>
				<createDt>2020-09-06 09:46:13.476</createDt>
				<deathCnt>3</deathCnt>
				<defCnt>293</defCnt>
				<gubun>대전</gubun>
				<gubunCn>大田</gubunCn>
				<gubunEn>Daejeon</gubunEn>
				<incDec>5</incDec>
				<isolClearCnt>197</isolClearCnt>
				<isolIngCnt>93</isolIngCnt>
				<localOccCnt>5</localOccCnt>
				<overFlowCnt>0</overFlowCnt>
				<qurRate>19.88</qurRate>
				<seq>4175</seq>
				<stdDay>2020년 09월 06일 00시</stdDay>
				<updateDt>null</updateDt>
			</item>
			<item>
				<createDt>2020-09-06 09:46:13.476</createDt>
				<deathCnt>2</deathCnt>
				<defCnt>420</defCnt>
				<gubun>광주</gubun>
				<gubunCn>光州</gubunCn>
				<gubunEn>Gwangju</gubunEn>
				<incDec>7</incDec>
				<isolClearCnt>274</isolClearCnt>
				<isolIngCnt>144</isolIngCnt>
				<localOccCnt>7</localOccCnt>
				<overFlowCnt>0</overFlowCnt>
				<qurRate>28.83</qurRate>
				<seq>4174</seq>
				<stdDay>2020년 09월 06일 00시</stdDay>
				<updateDt>null</updateDt>
			</item>
			<item>
				<createDt>2020-09-06 09:46:13.476</createDt>
				<deathCnt>3</deathCnt>
				<defCnt>796</defCnt>
				<gubun>인천</gubun>
				<gubunCn>仁川</gubunCn>
				<gubunEn>Incheon</gubunEn>
				<incDec>12</incDec>
				<isolClearCnt>492</isolClearCnt>
				<isolIngCnt>301</isolIngCnt>
				<localOccCnt>9</localOccCnt>
				<overFlowCnt>3</overFlowCnt>
				<qurRate>26.93</qurRate>
				<seq>4173</seq>
				<stdDay>2020년 09월 06일 00시</stdDay>
				<updateDt>null</updateDt>
			</item>
			<item>
				<createDt>2020-09-06 09:46:13.476</createDt>
				<deathCnt>191</deathCnt>
				<defCnt>7082</defCnt>
				<gubun>대구</gubun>
				<gubunCn>大邱</gubunCn>
				<gubunEn>Daegu</gubunEn>
				<incDec>5</incDec>
				<isolClearCnt>6785</isolClearCnt>
				<isolIngCnt>106</isolIngCnt>
				<localOccCnt>4</localOccCnt>
				<overFlowCnt>1</overFlowCnt>
				<qurRate>290.66</qurRate>
				<seq>4172</seq>
				<stdDay>2020년 09월 06일 00시</stdDay>
				<updateDt>null</updateDt>
			</item>
			<item>
				<createDt>2020-09-06 09:46:13.476</createDt>
				<deathCnt>4</deathCnt>
				<defCnt>331</defCnt>
				<gubun>부산</gubun>
				<gubunCn>釜山</gubunCn>
				<gubunEn>Busan</gubunEn>
				<incDec>2</incDec>
				<isolClearCnt>243</isolClearCnt>
				<isolIngCnt>84</isolIngCnt>
				<localOccCnt>2</localOccCnt>
				<overFlowCnt>0</overFlowCnt>
				<qurRate>9.70</qurRate>
				<seq>4171</seq>
				<stdDay>2020년 09월 06일 00시</stdDay>
				<updateDt>null</updateDt>
			</item>
			<item>
				<createDt>2020-09-06 09:46:13.475</createDt>
				<deathCnt>26</deathCnt>
				<defCnt>4314</defCnt>
				<gubun>서울</gubun>
				<gubunCn>首尔</gubunCn>
				<gubunEn>Seoul</gubunEn>
				<incDec>63</incDec>
				<isolClearCnt>2225</isolClearCnt>
				<isolIngCnt>2063</isolIngCnt>
				<localOccCnt>63</localOccCnt>
				<overFlowCnt>0</overFlowCnt>
				<qurRate>44.32</qurRate>
				<seq>4170</seq>
				<stdDay>2020년 09월 06일 00시</stdDay>
				<updateDt>null</updateDt>
			</item>
			<item>
				<createDt>2020-09-06 09:46:13.475</createDt>
				<deathCnt>334</deathCnt>
				<defCnt>21177</defCnt>
				<gubun>합계</gubun>
				<gubunCn>合计</gubunCn>
				<gubunEn>Total</gubunEn>
				<incDec>167</incDec>
				<isolClearCnt>16146</isolClearCnt>
				<isolIngCnt>4697</isolIngCnt>
				<localOccCnt>152</localOccCnt>
				<overFlowCnt>15</overFlowCnt>
				<qurRate>40.84</qurRate>
				<seq>4169</seq>
				<stdDay>2020년 09월 06일 00시</stdDay>
				<updateDt>null</updateDt>
			</item>
			<item>
				<createDt>2020-09-05 10:10:47.405</createDt>
				<deathCnt>0</deathCnt>
				<defCnt>1372</defCnt>
				<gubun>검역</gubun>
				<gubunCn>隔離區</gubunCn>
				<gubunEn>Lazaretto</gubunEn>
				<incDec>4</incDec>
				<isolClearCnt>1282</isolClearCnt>
				<isolIngCnt>90</isolIngCnt>
				<localOccCnt>0</localOccCnt>
				<overFlowCnt>4</overFlowCnt>
				<qurRate>-</qurRate>
				<seq>4168</seq>
				<stdDay>2020년 09월 05일 00시</stdDay>
				<updateDt>null</updateDt>
			</item>
			<item>
				<createDt>2020-09-05 10:10:47.405</createDt>
				<deathCnt>0</deathCnt>
				<defCnt>48</defCnt>
				<gubun>제주</gubun>
				<gubunCn>济州</gubunCn>
				<gubunEn>Jeju</gubunEn>
				<incDec>1</incDec>
				<isolClearCnt>27</isolClearCnt>
				<isolIngCnt>21</isolIngCnt>
				<localOccCnt>1</localOccCnt>
				<overFlowCnt>0</overFlowCnt>
				<qurRate>7.16</qurRate>
				<seq>4167</seq>
				<stdDay>2020년 09월 05일 00시</stdDay>
				<updateDt>null</updateDt>
			</item>
			<item>
				<createDt>2020-09-05 10:10:47.405</createDt>
				<deathCnt>0</deathCnt>
				<defCnt>251</defCnt>
				<gubun>경남</gubun>
				<gubunCn>庆南</gubunCn>
				<gubunEn>Gyeongsangnam-do</gubunEn>
				<incDec>8</incDec>
				<isolClearCnt>188</isolClearCnt>
				<isolIngCnt>63</isolIngCnt>
				<localOccCnt>8</localOccCnt>
				<overFlowCnt>0</overFlowCnt>
				<qurRate>7.47</qurRate>
				<seq>4166</seq>
				<stdDay>2020년 09월 05일 00시</stdDay>
				<updateDt>null</updateDt>
			</item>
			<item>
				<createDt>2020-09-05 10:10:47.405</createDt>
				<deathCnt>54</deathCnt>
				<defCnt>1473</defCnt>
				<gubun>경북</gubun>
				<gubunCn>庆北</gubunCn>
				<gubunEn>Gyeongsangbuk-do</gubunEn>
				<incDec>1</incDec>
				<isolClearCnt>1374</isolClearCnt>
				<isolIngCnt>45</isolIngCnt>
				<localOccCnt>0</localOccCnt>
				<overFlowCnt>1</overFlowCnt>
				<qurRate>55.32</qurRate>
				<seq>4165</seq>
				<stdDay>2020년 09월 05일 00시</stdDay>
				<updateDt>null</updateDt>
			</item>
			<item>
				<createDt>2020-09-05 10:10:47.404</createDt>
				<deathCnt>0</deathCnt>
				<defCnt>156</defCnt>
				<gubun>전남</gubun>
				<gubunCn>全南</gubunCn>
				<gubunEn>Jeollanam-do</gubunEn>
				<incDec>0</incDec>
				<isolClearCnt>47</isolClearCnt>
				<isolIngCnt>109</isolIngCnt>
				<localOccCnt>0</localOccCnt>
				<overFlowCnt>0</overFlowCnt>
				<qurRate>8.37</qurRate>
				<seq>4164</seq>
				<stdDay>2020년 09월 05일 00시</stdDay>
				<updateDt>null</updateDt>
			</item>
			<item>
				<createDt>2020-09-05 10:10:47.404</createDt>
				<deathCnt>verFlowCnt>
					<qurRate>4.9</qurRate>
					<seq>4163</seq>
					<stdDay>2020년 09월 05일 00시</stdDay>
					<updateDt>null</updateDt>
				</item>
				<item>
					<createDt>2020-09-05 10:10:47.404</createDt>
					<deathCnt>1</deathCnt>
					<defCnt>378</defCnt>
					<gubun>충남</gubun>
					<gubunCn>忠南</gubunCn>
					<gubunEn>Chungcheongnam-do</gubunEn>
					<incDec>4</incDec>
					<isolClearCnt>230</isolClearCnt>
					<isolIngCnt>147</isolIngCnt>
					<localOccCnt>4</localOccCnt>
					<overFlowCnt>0</overFlowCnt>
					<qurRate>17.81</qurRate>
					<seq>4162</seq>
					<stdDay>2020년 09월 05일 00시</stdDay>
					<updateDt>null</updateDt>
				</item>
				<item>
					<createDt>2020-09-05 10:10:47.404</createDt>
					<deathCnt>1</deathCnt>
					<defCnt>139</defCnt>
					<gubun>충북</gubun>
					<gubunCn>忠北</gubunCn>
					<gubunEn>Chungcheongbuk-do</gubunEn>
					<incDec>4</incDec>
					<isolClearCnt>94</isolClearCnt>
					<isolIngCnt>44</isolIngCnt>
					<localOccCnt>2</localOccCnt>
					<overFlowCnt>2</overFlowCnt>
					<qurRate>8.69</qurRate>
					<seq>4161</seq>
					<stdDay>2020년 09월 05일 00시
</stdDay>
					<updateDt>nul
PS C:\Users\IT\Documents\File Manipulator>  cd 'c:\Users\IT\Documents\File Manipulator'; & 'C:\Users\IT\AppData\Local\Programs\Python\Python38-32\python.exe' 'c:\Users\IT\.vscode\extensions\ms-python.python-2020.7.96456\pythonFiles\lib\python\debugpy\launcher' '1766' '--' 'c:\Users\IT\Documents\File Manipulator\Covid19\covid_by_city.py' 

						<?xml version="1.0" encoding="utf-8"?>
						<response>
							<header>
								<resultCode>00</resultCode>
								<resultMsg>NORMAL SERVICE.</resultMsg>
							</header>
							<body>
								<items>
									<item>
										<createDt>2020-09-06 09:46:13.478</createDt>
										<deathCnt>0</deathCnt>
										<defCnt>1376</defCnt>
										<gubun>검역</gubun>
										<gubunCn>隔離區</gubunCn>
										<gubunEn>Lazaretto</gubunEn>
										<incDec>4</incDec>
										<isolClearCnt>1283</isolClearCnt>
										<isolIngCnt>93</isolIngCnt>
										<localOccCnt>0</localOccCnt>
										<overFlowCnt>4</overFlowCnt>
										<qurRate>-</qurRate>
										<seq>4187</seq>
										<stdDay>2020년 09월 06일 00시</stdDay>
										<updateDt>null</updateDt>
									</item>
									<item>
										<createDt>2020-09-06 09:46:13.478</createDt>
										<deathCnt>0</deathCnt>
										<defCnt>48</defCnt>
										<gubun>제주</gubun>
										<gubunCn>济州</gubunCn>
										<gubunEn>Jeju</gubunEn>
										<incDec>0</incDec>
										<isolClearCnt>27</isolClearCnt>
										<isolIngCnt>21</isolIngCnt>
										<localOccCnt>0</localOccCnt>
										<overFlowCnt>0</overFlowCnt>
										<qurRate>7.16</qurRate>
										<seq>4186</seq>
										<stdDay>2020년 09월 06일 00시</stdDay>
										<updateDt>null</updateDt>
									</item>
									<item>
										<createDt>2020-09-06 09:46:13.478</createDt>
										<deathCnt>0</deathCnt>
										<defCnt>257</defCnt>
										<gubun>경남</gubun>
										<gubunCn>庆南</gubunCn>
										<gubunEn>Gyeongsangnam-do</gubunEn>
										<incDec>6</incDec>
										<isolClearCnt>194</isolClearCnt>
										<isolIngCnt>63</isolIngCnt>
										<localOccCnt>4</localOccCnt>
										<overFlowCnt>2</overFlowCnt>
										<qurRate>7.65</qurRate>
										<seq>4185</seq>
										<stdDay>2020년 09월 06일 00시</stdDay>
										<updateDt>null</updateDt>
									</item>
									<item>
										<createDt>2020-09-06 09:46:13.477</createDt>
										<deathCnt>54</deathCnt>
										<defCnt>1475</defCnt>
										<gubun>경북</gubun>
										<gubunCn>庆北</gubunCn>
										<gubunEn>Gyeongsangbuk-do</gubunEn>
										<incDec>2</incDec>
										<isolClearCnt>1376</isolClearCnt>
										<isolIngCnt>45</isolIngCnt>
										<localOccCnt>2</localOccCnt>
										<overFlowCnt>0</overFlowCnt>
										<qurRate>55.40</qurRate>
										<seq>4184</seq>
										<stdDay>2020년 09월 06일 00시</stdDay>
										<updateDt>null</updateDt>
									</item>
									<item>
										<createDt>2020-09-06 09:46:13.477</createDt>
										<deathCnt>0</deathCnt>
										<defCnt>159</defCnt>
										<gubun>전남</gubun>
										<gubunCn>全南</gubunCn>
										<gubunEn>Jeollanam-do</gubunEn>
										<incDec>3</incDec>
										<isolClearCnt>47</isolClearCnt>
										<isolIngCnt>112</isolIngCnt>
										<localOccCnt>0</localOccCnt>
										<overFlowCnt>3</overFlowCnt>
										<qurRate>8.53</qurRate>
										<seq>4183</seq>
										<stdDay>2020년 09월 06일 00시</stdDay>
										<updateDt>null</updateDt>
									</item>
									<item>
										<createDt>2020-09-06 09:46:13.477</createDt>
										<deathCnt>0</deathCnt>
										<defCnt>90</defCnt>
										<gubun>전북</gubun>
										<gubunCn>全北</gubunCn>
										<gubunEn>Jeollabuk-do</gubunEn>
										<incDec>1</incDec>
										<isolClearCnt>53</isolClearCnt>
										<isolIngCnt>37</isolIngCnt>
										<localOccCnt>1</localOccCnt>
										<overFlowCnt>0</overFlowCnt>
										<qurRate>4.95</qurRate>
										<seq>4182</seq>
										<stdDay>2020년 09월 06일 00시</stdDay>
										<updateDt>null</updateDt>
									</item>
									<item>
										<createDt>2020-09-06 09:46:13.477</createDt>
										<deathCnt>1</deathCnt>
										<defCnt>380</defCnt>
										<gubun>충남</gubun>
										<gubunCn>忠南</gubunCn>
										<gubunEn>Chungcheongnam-do</gubunEn>
										<incDec>2</incDec>
										<isolClearCnt>232</isolClearCnt>
										<isolIngCnt>147</isolIngCnt>
										<localOccCnt>2</localOccCnt>
										<overFlowCnt>0</overFlowCnt>
										<qurRate>17.90</qurRate>
										<seq>4181</seq>
										<stdDay>2020년 09월 06일 00시</stdDay>
										<updateDt>null</updateDt>
									</item>
									<item>
										<createDt>2020-09-06 09:46:13.477</createDt>
										<deathCnt>1</deathCnt>
										<defCnt>141</defCnt>
										<gubun>충북</gubun>
										<gubunCn>忠北</gubunCn>
										<gubunEn>Chungcheongbuk-do</gubunEn>
										<incDec>2</incDec>
										<isolClearCnt>99</isolClearCnt>
										<isolIngCnt>41</isolIngCnt>
										<localOccCnt>2</localOccCnt>
										<overFlowCnt>0</overFlowCnt>
										<qurRate>8.82</qurRate>
										<seq>4180</seq>
										<stdDay>2020년 09월 06일 00시</stdDay>
										<updateDt>null</updateDt>
									</item>
									<item>
										<createDt>2020-09-06 09:46:13.477</createDt>
										<deathCnt>3</deathCnt>
										<defCnt>210</defCnt>
										<gubun>강원</gubun>
										<gubunCn>江原</gubunCn>
										<gubunEn>Gangwon-do</gubunEn>
										<incDec>5</incDec>
										<isolClearCnt>133</isolClearCnt>
										<isolIngCnt>74</isolIngCnt>
										<localOccCnt>5</localOccCnt>
										<overFlowCnt>0</overFlowCnt>
										<qurRate>13.63</qurRate>
										<seq>4179</seq>
										<stdDay>2020년 09월 06일 00시</stdDay>
										<updateDt>null</updateDt>
									</item>
									<item>
										<createDt>2020-09-06 09:46:13.477</createDt>
										<deathCnt>45</deathCnt>
										<defCnt>3625</defCnt>
										<gubun>경기</gubun>
										<gubunCn>京畿</gubunCn>
										<gubunEn>Gyeonggi-do</gubunEn>
										<incDec>47</incDec>
										<isolClearCnt>2359</isolClearCnt>
										<isolIngCnt>1221</isolIngCnt>
										<localOccCnt>45</localOccCnt>
										<overFlowCnt>2</overFlowCnt>
										<qurRate>27.36</qurRate>
										<seq>4178</seq>
										<stdDay>2020년 09월 06일 00시</stdDay>
										<updateDt>null</updateDt>
									</item>
									<item>
										<createDt>2020-09-06 09:46:13.476</createDt>
										<deathCnt>0</deathCnt>
										<defCnt>67</defCnt>
										<gubun>세종</gubun>
										<gubunCn>世宗</gubunCn>
										<gubunEn>Sejong</gubunEn>
										<incDec>0</incDec>
										<isolClearCnt>58</isolClearCnt>
										<isolIngCnt>9</isolIngCnt>
										<localOccCnt>0</localOccCnt>
										<overFlowCnt>0</overFlowCnt>
										<qurRate>19.57</qurRate>
										<seq>4177</seq>
										<stdDay>2020년 09월 06일 00시</stdDay>
										<updateDt>null</updateDt>
									</item>
									<item>
										<createDt>2020-09-06 09:46:13.476</createDt>
										<deathCnt>1</deathCnt>
										<defCnt>113</defCnt>
										<gubun>울산</gubun>
										<gubunCn>蔚山</gubunCn>
										<gubunEn>Ulsan</gubunEn>
										<incDec>1</incDec>
										<isolClearCnt>69</isolClearCnt>
										<isolIngCnt>43</isolIngCnt>
										<localOccCnt>1</localOccCnt>
										<overFlowCnt>0</overFlowCnt>
										<qurRate>9.85</qurRate>
										<seq>4176</seq>
										<stdDay>2020년 09월 06일 00시</stdDay>
										<updateDt>null</updateDt>
									</item>
									<item>
										<createDt>2020-09-06 09:46:13.476</createDt>
										<deathCnt>3</deathCnt>
										<defCnt>293</defCnt>
										<gubun>대전</gubun>
										<gubunCn>大田</gubunCn>
										<gubunEn>Daejeon</gubunEn>
										<incDec>5</incDec>
										<isolClearCnt>197</isolClearCnt>
										<isolIngCnt>93</isolIngCnt>
										<localOccCnt>5</localOccCnt>
										<overFlowCnt>0</overFlowCnt>
										<qurRate>19.88</qurRate>
										<seq>4175</seq>
										<stdDay>2020년 09월 06일 00시</stdDay>
										<updateDt>null</updateDt>
									</item>
									<item>
										<createDt>2020-09-06 09:46:13.476</createDt>
										<deathCnt>2</deathCnt>
										<defCnt>420</defCnt>
										<gubun>광주</gubun>
										<gubunCn>光州</gubunCn>
										<gubunEn>Gwangju</gubunEn>
										<incDec>7</incDec>
										<isolClearCnt>274</isolClearCnt>
										<isolIngCnt>144</isolIngCnt>
										<localOccCnt>7</localOccCnt>
										<overFlowCnt>0</overFlowCnt>
										<qurRate>28.83</qurRate>
										<seq>4174</seq>
										<stdDay>2020년 09월 06일 00시</stdDay>
										<updateDt>null</updateDt>
									</item>
									<item>
										<createDt>2020-09-06 09:46:13.476</createDt>
										<deathCnt>3</deathCnt>
										<defCnt>796</defCnt>
										<gubun>인천</gubun>
										<gubunCn>仁川</gubunCn>
										<gubunEn>Incheon</gubunEn>
										<incDec>12</incDec>
										<isolClearCnt>492</isolClearCnt>
										<isolIngCnt>301</isolIngCnt>
										<localOccCnt>9</localOccCnt>
										<overFlowCnt>3</overFlowCnt>
										<qurRate>26.93</qurRate>
										<seq>4173</seq>
										<stdDay>2020년 09월 06일 00시</stdDay>
										<updateDt>null</updateDt>
									</item>
									<item>
										<createDt>2020-09-06 09:46:13.476</createDt>
										<deathCnt>191</deathCnt>
										<defCnt>7082</defCnt>
										<gubun>대구</gubun>
										<gubunCn>大邱</gubunCn>
										<gubunEn>Daegu</gubunEn>
										<incDec>5</incDec>
										<isolClearCnt>6785</isolClearCnt>
										<isolIngCnt>106</isolIngCnt>
										<localOccCnt>4</localOccCnt>
										<overFlowCnt>1</overFlowCnt>
										<qurRate>290.66</qurRate>
										<seq>4172</seq>
										<stdDay>2020년 09월 06일 00시</stdDay>
										<updateDt>null</updateDt>
									</item>
									<item>
										<createDt>2020-09-06 09:46:13.476</createDt>
										<deathCnt>4</deathCnt>
										<defCnt>331</defCnt>
										<gubun>부산</gubun>
										<gubunCn>釜山</gubunCn>
										<gubunEn>Busan</gubunEn>
										<incDec>2</incDec>
										<isolClearCnt>243</isolClearCnt>
										<isolIngCnt>84</isolIngCnt>
										<localOccCnt>2</localOccCnt>
										<overFlowCnt>0</overFlowCnt>
										<qurRate>9.70</qurRate>
										<seq>4171</seq>
										<stdDay>2020년 09월 06일 00시</stdDay>
										<updateDt>null</updateDt>
									</item>
									<item>
										<createDt>2020-09-06 09:46:13.475</createDt>
										<deathCnt>26</deathCnt>
										<defCnt>4314</defCnt>
										<gubun>서울</gubun>
										<gubunCn>首尔</gubunCn>
										<gubunEn>Seoul</gubunEn>
										<incDec>63</incDec>
										<isolClearCnt>2225</isolClearCnt>
										<isolIngCnt>2063</isolIngCnt>
										<localOccCnt>63</localOccCnt>
										<overFlowCnt>0</overFlowCnt>
										<qurRate>44.32</qurRate>
										<seq>4170</seq>
										<stdDay>2020년 09월 06일 00시</stdDay>
										<updateDt>null</updateDt>
									</item>
									<item>
										<createDt>2020-09-06 09:46:13.475</createDt>
										<deathCnt>334</deathCnt>
										<defCnt>21177</defCnt>
										<gubun>합계</gubun>
										<gubunCn>合计</gubunCn>
										<gubunEn>Total</gubunEn>
										<incDec>167</incDec>
										<isolClearCnt>16146</isolClearCnt>
										<isolIngCnt>4697</isolIngCnt>
										<localOccCnt>152</localOccCnt>
										<overFlowCnt>15</overFlowCnt>
										<qurRate>40.84</qurRate>
										<seq>4169</seq>
										<stdDay>2020년 09월 06일 00시</stdDay>
										<updateDt>null</updateDt>
									</item>
									<item>
										<createDt>2020-09-05 10:10:47.405</createDt>
										<deathCnt>0</deathCnt>
										<defCnt>1372</defCnt>
										<gubun>검역</gubun>
										<gubunCn>隔離區</gubunCn>
										<gubunEn>Lazaretto</gubunEn>
										<incDec>4</incDec>
										<isolClearCnt>1282</isolClearCnt>
										<isolIngCnt>90</isolIngCnt>
										<localOccCnt>0</localOccCnt>
										<overFlowCnt>4</overFlowCnt>
										<qurRate>-</qurRate>
										<seq>4168</seq>
										<stdDay>2020년 09월 05일 00시</stdDay>
										<updateDt>null</updateDt>
									</item>
									<item>
										<createDt>2020-09-05 10:10:47.405</createDt>
										<deathCnt>0</deathCnt>
										<defCnt>48</defCnt>
										<gubun>제주</gubun>
										<gubunCn>济州</gubunCn>
										<gubunEn>Jeju</gubunEn>
										<incDec>1</incDec>
										<isolClearCnt>27</isolClearCnt>
										<isolIngCnt>21</isolIngCnt>
										<localOccCnt>1</localOccCnt>
										<overFlowCnt>0</overFlowCnt>
										<qurRate>7.16</qurRate>
										<seq>4167</seq>
										<stdDay>2020년 09월 05일 00시</stdDay>
										<updateDt>null</updateDt>
									</item>
									<item>
										<createDt>2020-09-05 10:10:47.405</createDt>
										<deathCnt>0</deathCnt>
										<defCnt>251</defCnt>
										<gubun>경남</gubun>
										<gubunCn>庆南</gubunCn>
										<gubunEn>Gyeongsangnam-do</gubunEn>
										<incDec>8</incDec>
										<isolClearCnt>188</isolClearCnt>
										<isolIngCnt>63</isolIngCnt>
										<localOccCnt>8</localOccCnt>
										<overFlowCnt>0</overFlowCnt>
										<qurRate>7.47</qurRate>
										<seq>4166</seq>
										<stdDay>2020년 09월 05일 00시</stdDay>
										<updateDt>null</updateDt>
									</item>
									<item>
										<createDt>2020-09-05 10:10:47.405</createDt>
										<deathCnt>54</deathCnt>
										<defCnt>1473</defCnt>
										<gubun>경북</gubun>
										<gubunCn>庆北</gubunCn>
										<gubunEn>Gyeongsangbuk-do</gubunEn>
										<incDec>1</incDec>
										<isolClearCnt>1374</isolClearCnt>
										<isolIngCnt>45</isolIngCnt>
										<localOccCnt>0</localOccCnt>
										<overFlowCnt>1</overFlowCnt>
										<qurRate>55.32</qurRate>
										<seq>4165</seq>
										<stdDay>2020년 09월 05일 00시</stdDay>
										<updateDt>null</updateDt>
									</item>
									<item>
										<createDt>2020-09-05 10:10:47.404</createDt>
										<deathCnt>0</deathCnt>
										<defCnt>156</defCnt>
										<gubun>전남</gubun>
										<gubunCn>全南</gubunCn>
										<gubunEn>Jeollanam-do</gubunEn>
										<incDec>0</incDec>
										<isolClearCnt>47</isolClearCnt>
										<isolIngCnt>109</isolIngCnt>
										<localOccCnt>0</localOccCnt>
										<overFlowCnt>0</overFlowCnt>
										<qurRate>8.37</qurRate>
										<seq>4164</seq>
										<stdDay>2020년 09월 05일 00시</stdDay>
										<updateDt>null</updateDt>
									</item>
									<item>
										<createDt>2020-09-05 10:10:47.404</createDt>
										<deathCnt>0</deathCnt>
										<defCnt>89</defCnt>
										<gubun>전북</gubun>
										<gubunCn>全北</gubunCn>
										<gubunEn>Jeollabuk-do</gubunEn>
										<incDec>2</incDec>
										<isolClearCnt>53</isolClearCnt>
										<isolIngCnt>36</isolIngCnt>
										<localOccCnt>2</localOccCnt>
										<overFlowCnt>0</overFlowCnt>
										<qurRate>4.9</qurRate>
										<seq>4163</seq>
										<stdDay>2020년 09월 05일 00시</stdDay>
										<updateDt>null</updateDt>
									</item>
									<item>
										<createDt>2020-09-05 10:10:47.404</createDt>
										<deathCnt>1</deathCnt>
										<defCnt>378</defCnt>
										<gubun>충남</gubun>
										<gubunCn>忠南</gubunCn>
										<gubunEn>Chungcheongnam-do</gubunEn>
										<incDec>4</incDec>
										<isolClearCnt>230</isolClearCnt>
										<isolIngCnt>147</isolIngCnt>
										<localOccCnt>4</localOccCnt>
										<overFlowCnt>0</overFlowCnt>
										<qurRate>17.81</qurRate>
										<seq>4162</seq>
										<stdDay>2020년 09월 05일 00시</stdDay>
										<updateDt>null</updateDt>
									</item>
									<item>
										<createDt>2020-09-05 10:10:47.404</createDt>
										<deathCnt>1</deathCnt>
										<defCnt>139</defCnt>
										<gubun>충북</gubun>
										<gubunCn>忠北</gubunCn>
										<gubunEn>Chungcheongbuk-do</gubunEn>
										<incDec>4</incDec>
										<isolClearCnt>94</isolClearCnt>
										<isolIngCnt>44</isolIngCnt>
										<localOccCnt>2</localOccCnt>
										<overFlowCnt>2</overFlowCnt>
										<qurRate>8.69</qurRate>
										<seq>4161</seq>
										<stdDay>2020년 09월 05일 00시
</stdDay>
										<updateDt>nul
```
