var Module=typeof pyodide._module!=="undefined"?pyodide._module:{};Module.checkABI(1);if(!Module.expectedDataFileDownloads){Module.expectedDataFileDownloads=0;Module.finishedDataFileDownloads=0}Module.expectedDataFileDownloads++;(function(){var loadPackage=function(metadata){var PACKAGE_PATH;if(typeof window==="object"){PACKAGE_PATH=window["encodeURIComponent"](window.location.pathname.toString().substring(0,window.location.pathname.toString().lastIndexOf("/"))+"/")}else if(typeof location!=="undefined"){PACKAGE_PATH=encodeURIComponent(location.pathname.toString().substring(0,location.pathname.toString().lastIndexOf("/"))+"/")}else{throw"using preloaded data can only be done on a web page or in a web worker"}var PACKAGE_NAME="nose.data";var REMOTE_PACKAGE_BASE="nose.data";if(typeof Module["locateFilePackage"]==="function"&&!Module["locateFile"]){Module["locateFile"]=Module["locateFilePackage"];err("warning: you defined Module.locateFilePackage, that has been renamed to Module.locateFile (using your locateFilePackage for now)")}var REMOTE_PACKAGE_NAME=Module["locateFile"]?Module["locateFile"](REMOTE_PACKAGE_BASE,""):REMOTE_PACKAGE_BASE;var REMOTE_PACKAGE_SIZE=metadata.remote_package_size;var PACKAGE_UUID=metadata.package_uuid;function fetchRemotePackage(packageName,packageSize,callback,errback){var xhr=new XMLHttpRequest;xhr.open("GET",packageName,true);xhr.responseType="arraybuffer";xhr.onprogress=function(event){var url=packageName;var size=packageSize;if(event.total)size=event.total;if(event.loaded){if(!xhr.addedTotal){xhr.addedTotal=true;if(!Module.dataFileDownloads)Module.dataFileDownloads={};Module.dataFileDownloads[url]={loaded:event.loaded,total:size}}else{Module.dataFileDownloads[url].loaded=event.loaded}var total=0;var loaded=0;var num=0;for(var download in Module.dataFileDownloads){var data=Module.dataFileDownloads[download];total+=data.total;loaded+=data.loaded;num++}total=Math.ceil(total*Module.expectedDataFileDownloads/num);if(Module["setStatus"])Module["setStatus"]("Downloading data... ("+loaded+"/"+total+")")}else if(!Module.dataFileDownloads){if(Module["setStatus"])Module["setStatus"]("Downloading data...")}};xhr.onerror=function(event){throw new Error("NetworkError for: "+packageName)};xhr.onload=function(event){if(xhr.status==200||xhr.status==304||xhr.status==206||xhr.status==0&&xhr.response){var packageData=xhr.response;callback(packageData)}else{throw new Error(xhr.statusText+" : "+xhr.responseURL)}};xhr.send(null)}function handleError(error){console.error("package error:",error)}var fetchedCallback=null;var fetched=Module["getPreloadedPackage"]?Module["getPreloadedPackage"](REMOTE_PACKAGE_NAME,REMOTE_PACKAGE_SIZE):null;if(!fetched)fetchRemotePackage(REMOTE_PACKAGE_NAME,REMOTE_PACKAGE_SIZE,function(data){if(fetchedCallback){fetchedCallback(data);fetchedCallback=null}else{fetched=data}},handleError);function runWithFS(){function assert(check,msg){if(!check)throw msg+(new Error).stack}Module["FS_createPath"]("/","man",true,true);Module["FS_createPath"]("/man","man1",true,true);Module["FS_createPath"]("/","lib",true,true);Module["FS_createPath"]("/lib","python3.7",true,true);Module["FS_createPath"]("/lib/python3.7","site-packages",true,true);Module["FS_createPath"]("/lib/python3.7/site-packages","nose-1.3.7-py3.7.egg-info",true,true);Module["FS_createPath"]("/lib/python3.7/site-packages","nose",true,true);Module["FS_createPath"]("/lib/python3.7/site-packages/nose","ext",true,true);Module["FS_createPath"]("/lib/python3.7/site-packages/nose","plugins",true,true);Module["FS_createPath"]("/lib/python3.7/site-packages/nose","sphinx",true,true);Module["FS_createPath"]("/lib/python3.7/site-packages/nose","tools",true,true);Module["FS_createPath"]("/","bin",true,true);function DataRequest(start,end,audio){this.start=start;this.end=end;this.audio=audio}DataRequest.prototype={requests:{},open:function(mode,name){this.name=name;this.requests[name]=this;Module["addRunDependency"]("fp "+this.name)},send:function(){},onload:function(){var byteArray=this.byteArray.subarray(this.start,this.end);this.finish(byteArray)},finish:function(byteArray){var that=this;Module["FS_createPreloadedFile"](this.name,null,byteArray,true,true,function(){Module["removeRunDependency"]("fp "+that.name)},function(){if(that.audio){Module["removeRunDependency"]("fp "+that.name)}else{err("Preloading file "+that.name+" failed")}},false,true);this.requests[this.name]=null}};function processPackageData(arrayBuffer){Module.finishedDataFileDownloads++;assert(arrayBuffer,"Loading data file failed.");assert(arrayBuffer instanceof ArrayBuffer,"bad input to processPackageData");var byteArray=new Uint8Array(arrayBuffer);var curr;var compressedData={data:null,cachedOffset:297775,cachedIndexes:[-1,-1],cachedChunks:[null,null],offsets:[0,1284,2682,4106,5394,6620,7836,8924,10256,11601,12364,12958,13452,14040,14565,15187,16057,16832,18294,19662,20832,22041,23076,24102,25049,26321,27445,28654,29614,30850,32169,33201,34493,35557,36605,37853,39061,40348,41548,42730,43965,45150,46480,48003,49510,50689,51868,53030,54292,55600,56780,58130,59311,60606,61747,62854,64123,65511,66987,68226,69127,70408,71378,72533,73557,74874,75813,76940,78104,79134,80257,81264,82453,83747,85060,86185,87133,88379,89593,90741,91873,93078,94403,95650,96966,98327,99498,100655,102082,103384,104692,105929,107212,108421,109519,110652,111658,112865,114081,115124,116071,117166,118217,119185,120512,121762,122596,123959,125455,126456,127762,129143,130483,131810,133096,134186,135566,136772,138066,139432,140545,141772,143057,144251,145372,146342,147472,148686,149603,150786,151949,152980,154299,155428,156658,157828,159112,160170,161366,162819,164164,165494,166865,168093,169086,170275,171576,172887,174081,175419,176822,177647,178472,179427,180328,181433,182842,184121,185365,186376,187403,188320,189576,190821,192263,193564,194933,196398,197699,198925,200240,201515,202812,204121,205531,206825,208219,209522,210648,211725,213013,214236,215364,216497,217727,219137,220389,221477,222680,223768,224784,225841,227180,228622,229681,230807,231931,233016,234222,235388,236515,237844,239031,240246,241368,242493,243852,245057,246330,247260,248396,249618,250535,251723,252790,254016,255120,256075,256914,258338,259450,260518,261935,263406,264902,266173,267159,268253,269314,270466,271487,272429,273426,274559,275790,276996,278072,279021,280143,281297,282539,283832,285044,285924,287215,288304,289359,290665,291885,292859,294226,295593,296846],sizes:[1284,1398,1424,1288,1226,1216,1088,1332,1345,763,594,494,588,525,622,870,775,1462,1368,1170,1209,1035,1026,947,1272,1124,1209,960,1236,1319,1032,1292,1064,1048,1248,1208,1287,1200,1182,1235,1185,1330,1523,1507,1179,1179,1162,1262,1308,1180,1350,1181,1295,1141,1107,1269,1388,1476,1239,901,1281,970,1155,1024,1317,939,1127,1164,1030,1123,1007,1189,1294,1313,1125,948,1246,1214,1148,1132,1205,1325,1247,1316,1361,1171,1157,1427,1302,1308,1237,1283,1209,1098,1133,1006,1207,1216,1043,947,1095,1051,968,1327,1250,834,1363,1496,1001,1306,1381,1340,1327,1286,1090,1380,1206,1294,1366,1113,1227,1285,1194,1121,970,1130,1214,917,1183,1163,1031,1319,1129,1230,1170,1284,1058,1196,1453,1345,1330,1371,1228,993,1189,1301,1311,1194,1338,1403,825,825,955,901,1105,1409,1279,1244,1011,1027,917,1256,1245,1442,1301,1369,1465,1301,1226,1315,1275,1297,1309,1410,1294,1394,1303,1126,1077,1288,1223,1128,1133,1230,1410,1252,1088,1203,1088,1016,1057,1339,1442,1059,1126,1124,1085,1206,1166,1127,1329,1187,1215,1122,1125,1359,1205,1273,930,1136,1222,917,1188,1067,1226,1104,955,839,1424,1112,1068,1417,1471,1496,1271,986,1094,1061,1152,1021,942,997,1133,1231,1206,1076,949,1122,1154,1242,1293,1212,880,1291,1089,1055,1306,1220,974,1367,1367,1253,929],successes:[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]};compressedData.data=byteArray;assert(typeof Module.LZ4==="object","LZ4 not present - was your app build with  -s LZ4=1  ?");Module.LZ4.loadPackage({metadata:metadata,compressedData:compressedData});Module["removeRunDependency"]("datafile_nose.data")}Module["addRunDependency"]("datafile_nose.data");if(!Module.preloadResults)Module.preloadResults={};Module.preloadResults[PACKAGE_NAME]={fromCache:false};if(fetched){processPackageData(fetched);fetched=null}else{fetchedCallback=processPackageData}}if(Module["calledRun"]){runWithFS()}else{if(!Module["preRun"])Module["preRun"]=[];Module["preRun"].push(runWithFS)}};loadPackage({files:[{filename:"/man/man1/nosetests.1",start:0,end:17679,audio:0},{filename:"/lib/python3.7/site-packages/nose-1.3.7-py3.7.egg-info/SOURCES.txt",start:17679,end:34692,audio:0},{filename:"/lib/python3.7/site-packages/nose-1.3.7-py3.7.egg-info/entry_points.txt",start:34692,end:34825,audio:0},{filename:"/lib/python3.7/site-packages/nose-1.3.7-py3.7.egg-info/dependency_links.txt",start:34825,end:34826,audio:0},{filename:"/lib/python3.7/site-packages/nose-1.3.7-py3.7.egg-info/top_level.txt",start:34826,end:34831,audio:0},{filename:"/lib/python3.7/site-packages/nose-1.3.7-py3.7.egg-info/PKG-INFO",start:34831,end:36806,audio:0},{filename:"/lib/python3.7/site-packages/nose-1.3.7-py3.7.egg-info/not-zip-safe",start:36806,end:36807,audio:0},{filename:"/lib/python3.7/site-packages/nose/suite.py",start:36807,end:59121,audio:0},{filename:"/lib/python3.7/site-packages/nose/importer.py",start:59121,end:65099,audio:0},{filename:"/lib/python3.7/site-packages/nose/util.py",start:65099,end:85433,audio:0},{filename:"/lib/python3.7/site-packages/nose/usage.txt",start:85433,end:89858,audio:0},{filename:"/lib/python3.7/site-packages/nose/case.py",start:89858,end:103039,audio:0},{filename:"/lib/python3.7/site-packages/nose/__main__.py",start:103039,end:103183,audio:0},{filename:"/lib/python3.7/site-packages/nose/__init__.py",start:103183,end:103587,audio:0},{filename:"/lib/python3.7/site-packages/nose/core.py",start:103587,end:116658,audio:0},{filename:"/lib/python3.7/site-packages/nose/commands.py",start:116658,end:122974,audio:0},{filename:"/lib/python3.7/site-packages/nose/config.py",start:122974,end:148256,audio:0},{filename:"/lib/python3.7/site-packages/nose/failure.py",start:148256,end:149529,audio:0},{filename:"/lib/python3.7/site-packages/nose/selector.py",start:149529,end:158514,audio:0},{filename:"/lib/python3.7/site-packages/nose/result.py",start:158514,end:165255,audio:0},{filename:"/lib/python3.7/site-packages/nose/twistedtools.py",start:165255,end:170795,audio:0},{filename:"/lib/python3.7/site-packages/nose/pyversion.py",start:170795,end:178249,audio:0},{filename:"/lib/python3.7/site-packages/nose/exc.py",start:178249,end:178625,audio:0},{filename:"/lib/python3.7/site-packages/nose/inspector.py",start:178625,end:185600,audio:0},{filename:"/lib/python3.7/site-packages/nose/loader.py",start:185600,end:211087,audio:0},{filename:"/lib/python3.7/site-packages/nose/proxy.py",start:211087,end:217966,audio:0},{filename:"/lib/python3.7/site-packages/nose/ext/__init__.py",start:217966,end:217999,audio:0},{filename:"/lib/python3.7/site-packages/nose/ext/dtcompat.py",start:217999,end:306112,audio:0},{filename:"/lib/python3.7/site-packages/nose/plugins/cover.py",start:306112,end:317789,audio:0},{filename:"/lib/python3.7/site-packages/nose/plugins/xunit.py",start:317789,end:329434,audio:0},{filename:"/lib/python3.7/site-packages/nose/plugins/collect.py",start:329434,end:332547,audio:0},{filename:"/lib/python3.7/site-packages/nose/plugins/deprecated.py",start:332547,end:334098,audio:0},{filename:"/lib/python3.7/site-packages/nose/plugins/isolate.py",start:334098,end:337854,audio:0},{filename:"/lib/python3.7/site-packages/nose/plugins/__init__.py",start:337854,end:344145,audio:0},{filename:"/lib/python3.7/site-packages/nose/plugins/plugintest.py",start:344145,end:357678,audio:0},{filename:"/lib/python3.7/site-packages/nose/plugins/builtin.py",start:357678,end:358699,audio:0},{filename:"/lib/python3.7/site-packages/nose/plugins/errorclass.py",start:358699,end:365974,audio:0},{filename:"/lib/python3.7/site-packages/nose/plugins/testid.py",start:365974,end:375891,audio:0},{filename:"/lib/python3.7/site-packages/nose/plugins/manager.py",start:375891,end:391468,audio:0},{filename:"/lib/python3.7/site-packages/nose/plugins/doctests.py",start:391468,end:408946,audio:0},{filename:"/lib/python3.7/site-packages/nose/plugins/skip.py",start:408946,end:411088,audio:0},{filename:"/lib/python3.7/site-packages/nose/plugins/logcapture.py",start:411088,end:420446,audio:0},{filename:"/lib/python3.7/site-packages/nose/plugins/base.py",start:420446,end:446504,audio:0},{filename:"/lib/python3.7/site-packages/nose/plugins/allmodules.py",start:446504,end:448224,audio:0},{filename:"/lib/python3.7/site-packages/nose/plugins/prof.py",start:448224,end:453581,audio:0},{filename:"/lib/python3.7/site-packages/nose/plugins/multiprocess.py",start:453581,end:488867,audio:0},{filename:"/lib/python3.7/site-packages/nose/plugins/attrib.py",start:488867,end:498533,audio:0},{filename:"/lib/python3.7/site-packages/nose/plugins/capture.py",start:498533,end:501897,audio:0},{filename:"/lib/python3.7/site-packages/nose/plugins/debug.py",start:501897,end:504169,audio:0},{filename:"/lib/python3.7/site-packages/nose/plugins/failuredetail.py",start:504169,end:505804,audio:0},{filename:"/lib/python3.7/site-packages/nose/sphinx/__init__.py",start:505804,end:505809,audio:0},{filename:"/lib/python3.7/site-packages/nose/sphinx/pluginopts.py",start:505809,end:511447,audio:0},{filename:"/lib/python3.7/site-packages/nose/tools/trivial.py",start:511447,end:512631,audio:0},{filename:"/lib/python3.7/site-packages/nose/tools/__init__.py",start:512631,end:513067,audio:0},{filename:"/lib/python3.7/site-packages/nose/tools/nontrivial.py",start:513067,end:517237,audio:0},{filename:"/bin/nosetests",start:517237,end:517639,audio:0},{filename:"/bin/nosetests-3.7",start:517639,end:518049,audio:0}],remote_package_size:301871,package_uuid:"fd0c1a26-470b-4fb5-a868-837bcc1c0dfe"})})();