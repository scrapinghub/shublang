var Module=typeof pyodide._module!=="undefined"?pyodide._module:{};Module.checkABI(1);if(!Module.expectedDataFileDownloads){Module.expectedDataFileDownloads=0;Module.finishedDataFileDownloads=0}Module.expectedDataFileDownloads++;(function(){var loadPackage=function(metadata){var PACKAGE_PATH;if(typeof window==="object"){PACKAGE_PATH=window["encodeURIComponent"](window.location.pathname.toString().substring(0,window.location.pathname.toString().lastIndexOf("/"))+"/")}else if(typeof location!=="undefined"){PACKAGE_PATH=encodeURIComponent(location.pathname.toString().substring(0,location.pathname.toString().lastIndexOf("/"))+"/")}else{throw"using preloaded data can only be done on a web page or in a web worker"}var PACKAGE_NAME="convertdate.data";var REMOTE_PACKAGE_BASE="convertdate.data";if(typeof Module["locateFilePackage"]==="function"&&!Module["locateFile"]){Module["locateFile"]=Module["locateFilePackage"];err("warning: you defined Module.locateFilePackage, that has been renamed to Module.locateFile (using your locateFilePackage for now)")}var REMOTE_PACKAGE_NAME=Module["locateFile"]?Module["locateFile"](REMOTE_PACKAGE_BASE,""):REMOTE_PACKAGE_BASE;var REMOTE_PACKAGE_SIZE=metadata.remote_package_size;var PACKAGE_UUID=metadata.package_uuid;function fetchRemotePackage(packageName,packageSize,callback,errback){var xhr=new XMLHttpRequest;xhr.open("GET",packageName,true);xhr.responseType="arraybuffer";xhr.onprogress=function(event){var url=packageName;var size=packageSize;if(event.total)size=event.total;if(event.loaded){if(!xhr.addedTotal){xhr.addedTotal=true;if(!Module.dataFileDownloads)Module.dataFileDownloads={};Module.dataFileDownloads[url]={loaded:event.loaded,total:size}}else{Module.dataFileDownloads[url].loaded=event.loaded}var total=0;var loaded=0;var num=0;for(var download in Module.dataFileDownloads){var data=Module.dataFileDownloads[download];total+=data.total;loaded+=data.loaded;num++}total=Math.ceil(total*Module.expectedDataFileDownloads/num);if(Module["setStatus"])Module["setStatus"]("Downloading data... ("+loaded+"/"+total+")")}else if(!Module.dataFileDownloads){if(Module["setStatus"])Module["setStatus"]("Downloading data...")}};xhr.onerror=function(event){throw new Error("NetworkError for: "+packageName)};xhr.onload=function(event){if(xhr.status==200||xhr.status==304||xhr.status==206||xhr.status==0&&xhr.response){var packageData=xhr.response;callback(packageData)}else{throw new Error(xhr.statusText+" : "+xhr.responseURL)}};xhr.send(null)}function handleError(error){console.error("package error:",error)}var fetchedCallback=null;var fetched=Module["getPreloadedPackage"]?Module["getPreloadedPackage"](REMOTE_PACKAGE_NAME,REMOTE_PACKAGE_SIZE):null;if(!fetched)fetchRemotePackage(REMOTE_PACKAGE_NAME,REMOTE_PACKAGE_SIZE,function(data){if(fetchedCallback){fetchedCallback(data);fetchedCallback=null}else{fetched=data}},handleError);function runWithFS(){function assert(check,msg){if(!check)throw msg+(new Error).stack}Module["FS_createPath"]("/","lib",true,true);Module["FS_createPath"]("/lib","python3.7",true,true);Module["FS_createPath"]("/lib/python3.7","site-packages",true,true);Module["FS_createPath"]("/lib/python3.7/site-packages","convertdate",true,true);Module["FS_createPath"]("/lib/python3.7/site-packages/convertdate","data",true,true);Module["FS_createPath"]("/lib/python3.7/site-packages","convertdate-2.2.0-py3.7.egg-info",true,true);function DataRequest(start,end,audio){this.start=start;this.end=end;this.audio=audio}DataRequest.prototype={requests:{},open:function(mode,name){this.name=name;this.requests[name]=this;Module["addRunDependency"]("fp "+this.name)},send:function(){},onload:function(){var byteArray=this.byteArray.subarray(this.start,this.end);this.finish(byteArray)},finish:function(byteArray){var that=this;Module["FS_createPreloadedFile"](this.name,null,byteArray,true,true,function(){Module["removeRunDependency"]("fp "+that.name)},function(){if(that.audio){Module["removeRunDependency"]("fp "+that.name)}else{err("Preloading file "+that.name+" failed")}},false,true);this.requests[this.name]=null}};function processPackageData(arrayBuffer){Module.finishedDataFileDownloads++;assert(arrayBuffer,"Loading data file failed.");assert(arrayBuffer instanceof ArrayBuffer,"bad input to processPackageData");var byteArray=new Uint8Array(arrayBuffer);var curr;var compressedData={data:null,cachedOffset:53625,cachedIndexes:[-1,-1],cachedChunks:[null,null],offsets:[0,1351,2437,3610,4908,6110,7493,8910,10009,11142,12512,13574,15004,16143,17477,18770,19880,21063,22266,23617,24925,26017,27387,28526,29582,30905,32087,33332,34513,35571,36356,36936,38063,39249,40485,41822,43177,44316,45496,46355,47232,48083,49294,50385,51572,52707],sizes:[1351,1086,1173,1298,1202,1383,1417,1099,1133,1370,1062,1430,1139,1334,1293,1110,1183,1203,1351,1308,1092,1370,1139,1056,1323,1182,1245,1181,1058,785,580,1127,1186,1236,1337,1355,1139,1180,859,877,851,1211,1091,1187,1135,918],successes:[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]};compressedData.data=byteArray;assert(typeof Module.LZ4==="object","LZ4 not present - was your app build with  -s LZ4=1  ?");Module.LZ4.loadPackage({metadata:metadata,compressedData:compressedData});Module["removeRunDependency"]("datafile_convertdate.data")}Module["addRunDependency"]("datafile_convertdate.data");if(!Module.preloadResults)Module.preloadResults={};Module.preloadResults[PACKAGE_NAME]={fromCache:false};if(fetched){processPackageData(fetched);fetched=null}else{fetchedCallback=processPackageData}}if(Module["calledRun"]){runWithFS()}else{if(!Module["preRun"])Module["preRun"]=[];Module["preRun"].push(runWithFS)}};loadPackage({files:[{filename:"/lib/python3.7/site-packages/convertdate/mayan.py",start:0,end:8327,audio:0},{filename:"/lib/python3.7/site-packages/convertdate/utils.py",start:8327,end:11461,audio:0},{filename:"/lib/python3.7/site-packages/convertdate/julianday.py",start:11461,end:13173,audio:0},{filename:"/lib/python3.7/site-packages/convertdate/french_republican.py",start:13173,end:23105,audio:0},{filename:"/lib/python3.7/site-packages/convertdate/bahai.py",start:23105,end:26577,audio:0},{filename:"/lib/python3.7/site-packages/convertdate/indian_civil.py",start:26577,end:29628,audio:0},{filename:"/lib/python3.7/site-packages/convertdate/__init__.py",start:29628,end:30909,audio:0},{filename:"/lib/python3.7/site-packages/convertdate/daycount.py",start:30909,end:32041,audio:0},{filename:"/lib/python3.7/site-packages/convertdate/gregorian.py",start:32041,end:35135,audio:0},{filename:"/lib/python3.7/site-packages/convertdate/iso.py",start:35135,end:36760,audio:0},{filename:"/lib/python3.7/site-packages/convertdate/julian.py",start:36760,end:39269,audio:0},{filename:"/lib/python3.7/site-packages/convertdate/positivist.py",start:39269,end:43203,audio:0},{filename:"/lib/python3.7/site-packages/convertdate/persian.py",start:43203,end:45610,audio:0},{filename:"/lib/python3.7/site-packages/convertdate/islamic.py",start:45610,end:47252,audio:0},{filename:"/lib/python3.7/site-packages/convertdate/dublin.py",start:47252,end:47908,audio:0},{filename:"/lib/python3.7/site-packages/convertdate/ordinal.py",start:47908,end:48990,audio:0},{filename:"/lib/python3.7/site-packages/convertdate/hebrew.py",start:48990,end:53209,audio:0},{filename:"/lib/python3.7/site-packages/convertdate/coptic.py",start:53209,end:54952,audio:0},{filename:"/lib/python3.7/site-packages/convertdate/holidays.py",start:54952,end:63960,audio:0},{filename:"/lib/python3.7/site-packages/convertdate/data/__init__.py",start:63960,end:63960,audio:0},{filename:"/lib/python3.7/site-packages/convertdate/data/positivist.py",start:63960,end:76397,audio:0},{filename:"/lib/python3.7/site-packages/convertdate/data/french_republican_days.py",start:76397,end:84410,audio:0},{filename:"/lib/python3.7/site-packages/convertdate-2.2.0-py3.7.egg-info/SOURCES.txt",start:84410,end:85225,audio:0},{filename:"/lib/python3.7/site-packages/convertdate-2.2.0-py3.7.egg-info/dependency_links.txt",start:85225,end:85226,audio:0},{filename:"/lib/python3.7/site-packages/convertdate-2.2.0-py3.7.egg-info/requires.txt",start:85226,end:85265,audio:0},{filename:"/lib/python3.7/site-packages/convertdate-2.2.0-py3.7.egg-info/zip-safe",start:85265,end:85266,audio:0},{filename:"/lib/python3.7/site-packages/convertdate-2.2.0-py3.7.egg-info/top_level.txt",start:85266,end:85278,audio:0},{filename:"/lib/python3.7/site-packages/convertdate-2.2.0-py3.7.egg-info/PKG-INFO",start:85278,end:94069,audio:0}],remote_package_size:57721,package_uuid:"ede95497-e077-463f-be73-8e1b77f163a7"})})();