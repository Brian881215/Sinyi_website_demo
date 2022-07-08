$(function(){

    // 一級選單：l1_1
    // 二級選單：l2_1
    let selection = ["l1_1","l2_1"];
    // 二級選單項目
    const l2_items = [
        [],
        ["台北市","新北市","桃園市","大新竹","大台中","台南市","高雄市"],
        ["試用人員","2年以上正式人員","2-5年正式人員","5年以上正式人員"],
        ["業務人員","二級專員","一級專員","主任","專經以上"]
    ]

    var tip = d3.select("#tip");

    // section1
    const section1 = () =>{

    }
    // section2
    const section2 = () =>{  
        const svgSize={ width: 618,height: 80 };
        const margin = { top: 12, right: 34, bottom: 18, left: 36 };
        var width = svgSize.width - margin.left - margin.right;
        var height = svgSize.height - margin.top - margin.bottom;

        // 建立 svg 畫布
        var svg = d3
        .select("#section2 .d_chart")
        .append("svg")
        .attr("width", svgSize.width)
        .attr("height", svgSize.height)
        // 建立圖表群組
        var chart = svg
        .append("g")
        .attr("transform",`translate(${margin.left},${margin.top})`)
        .attr("class","pd_data_chart");

        // 匯入資料
        d3.json("./data/data.json")
        .then(data=>{
            
            let n_data=data["section2"]["info2"];

            // 製作比例尺
            var xScale = d3.scaleBand()
                        .domain(n_data.map(d => d.week))
                        .range([0, width]);

            var yScale = d3.scaleLinear()
                        .domain([0, (d3.max(n_data,d=>d.value)+25)])
                        .range([height, 0])
            // 建立座標軸
            var axisX = d3.axisBottom(xScale)
                          .tickSize(0)
                          .tickPadding(7)
            var axisY = d3.axisLeft(yScale)
                          .tickFormat(" ")
                          .tickSize(0);
            
            chart.append("g")
            .call(axisX)
            .attr("transform", `translate(0,${height})`);
            chart.append("g")
            .call(axisY)

            chart.append("text")
                .attr("y", height+14)
                .attr("x", width+10 )
                .attr("text-anchor", "start")
                .attr("font-size",14)
                .text("週");
            chart.append("text")
                .attr("x", -6)
                .attr("y", "20")
                .attr("text-anchor", "end")
                .attr("font-size",14)
                .text("人數");

            // 計算折線端點座標
            var line = d3.line()
                        .x(d => xScale(d.week))
                        .y(d => yScale(d.value));

            var gPath = chart.append("g")
                        .style("transform", "translate(22px,0)");

            gPath.append("path")
                .datum(n_data)
                .attr("class", "line")
                .attr("d", line)
                .style("fill", "none")
                .style("stroke", "#75CDD280")
                .style("stroke-width", "1.7px");

            gPath.selectAll("circle")
                .data(n_data)
                .enter()
                .append("circle")
                .attr("class", "dot")
                .attr("cx", d => xScale(d.week))
                .attr("cy", d => yScale(d.value))
                .attr("r", 3.2)
                .style("fill", "#23989F")

            gPath.selectAll("text")
                .data(n_data)
                .enter()
                .append("text")
                .attr("x", d => xScale(d.week))
                .attr("y", d => yScale(d.value)-10)
                .attr("text-anchor", "middle")
                .style("fill", "#23989F")
                .attr("font-size",14.5)
                .style("font-weight", "500")
                .text(d => d.value)
        })
        .catch(error => {
            console.log(error);
        });
    }
    // section3
    const section3_1 = () => {
    // 變數宣告
    const svgSize={ width: 940,height: 338 };
    const margin = { top: 40, right: 100, bottom: 35, left: 70 };
    var width = svgSize.width - margin.left - margin.right;
    var height = svgSize.height - margin.top - margin.bottom;

    // 堆疊圖結構色票
    var colors = ["#C2F1F4", "#79E0CF", "#2BB5C8"];
    // 建立 svg 畫布
    var svg = d3
        .select("body")
        .select("#section3 .d_chart")
        .append("svg") 
        .attr("width", svgSize.width)
        .attr("height", svgSize.height)
    // 建立圖表群組
    var chart = svg
        .append("g")
        .attr("transform",`translate(${margin.left},${margin.top})`)
        .attr("class","pd_data_chart2");

    d3.json("data/data.json")
      .then(data => {
        let n_data=data["section3_1"];
        // 週
        var weeksName = n_data["stack"].map(d=>d.week);
        // 常態使用人數總和
        var counts = n_data["stack"].map(d=>d.value);
        // 總和陣列
        var sum=[];
        counts.forEach((d,i)=>{
            sum[i]=d.value1+d.value2+d.value3;
        })

        // 製作比例尺
        var xScale = d3.scaleBand()
                    .domain(weeksName) 
                    .range([0, width])
                    .paddingInner(0.4)
                    .paddingOuter(0.35);

        var yScale = d3.scaleLinear()
                    .domain([0, d3.max(counts, d => d.value1 + d.value2 + d.value3)+40])
                    .range([height, 0]);
        var yScale2 = d3.scaleLinear()
                    .domain([0, 100])
                    .range([height, 0]);

        // 建立座標軸
        var axisX = d3.axisBottom(xScale)
                    .tickPadding(10)
        var axisY = d3.axisLeft(yScale)
                    .tickFormat(d => d+" 人")
        
        chart.append("g")
            .call(axisX)
            .attr("transform", `translate(0,${height})`);
        chart.append("g")
            .call(axisY)
        chart.append("text")
            .attr("y", 285)
            .attr("x", width+15)
            .text("週");
        chart.append("text")
            .attr("x", "30px")
            .attr("y", "-20px")
            .attr("text-anchor", "end")
            .text("常態使用人數");

        // 文字顯示
        chart.append("g")
             .attr("class","pd_data_chart2_text")
             .selectAll("text")
             .data(sum)
             .enter()
             .append("text")
             .attr("x",(d,i)=> xScale(weeksName[i])+5.5)
             .attr("y",(d,i)=> yScale(d)-6)
             .attr("font-weight", "500")
             .style("fill", "#666666")
             .text(d=>(d));

        // 進行分組
        const stack = d3.stack().keys(["value1", "value2", "value3"]);

        var groups = chart.selectAll(".stack")
                        .data(stack(counts))
                        .enter()
                        .append("g")
                        .attr("class", "stack")
                        .style("fill", (d, i) => colors[i]);
        groups.selectAll("rect")
                .data(d => d)
                .enter()
                .append("rect")
                .attr("x", (d, i) => xScale(weeksName[i]))
                .attr("y", d => yScale(d[1]))
                .attr("width", xScale.bandwidth())
                .attr("height", d => yScale(d[0]) - yScale(d[1]))
        // 畫折線圖
        var line = d3.line()
                     .x(d => xScale(d.week))
                     .y(d => (yScale2(d.percentage)));
        var gPath = chart.append("g")
                         .style("transform", "translate(18px,0)");
        gPath.append("path")
                         .datum(n_data["line"])
                         .attr("class", "line")
                         .attr("d", line)
                         .style("fill", "none")
                         .style("stroke", "#75CDD2")
                         .style("stroke-width", "2.5px");
        gPath.selectAll("circle")
                         .data(n_data["line"])
                         .enter()
                         .append("circle")
                         .attr("class", "dot")
                         .attr("cx", d => xScale(d.week))
                         .attr("cy", d => yScale2(d.percentage))
                         .attr("r", 5)
                         .style("fill", "#23989F")
                         .on("mouseover",(e,d)=>{
                            // console.log(e);
                            // console.log(d);
                            // console.log(yScale2(d.percentage));
                            d3.select("#tip").style("visibility","visible")
                                             .style("top",yScale2(d.percentage)-11+"px")
                                             .style("left",xScale(d.week)+"px")
                            d3.select("#tip_info1").text(d.value3);
                            d3.select("#tip_info2").text(d.value28);

                         })
                         .on("mouseout",(e,d)=>{
                            d3.select("#tip").style("visibility","hidden")
                         })
        gPath.selectAll("text")
                         .data(n_data["line"])
                         .enter()
                         .append("text")
                         .attr("x", d => xScale(d.week))
                         .attr("y", d => yScale2(d.percentage)-14)
                         .attr("text-anchor", "middle")
                         .style("fill", "#666666")
                         .attr("font-size",14.5)
                         .style("font-weight", "500")
                         .text(d => d.percentage+"%")
      })
      .catch(error => {
        console.log(error);
      });
    }
    const section3_2 = () => {
        // 變數宣告
        const svgSize={ width: 940,height: 338 };
        const margin = { top: 40, right: 100, bottom: 35, left: 70 };
        var width = svgSize.width - margin.left - margin.right;
        var height = svgSize.height - margin.top - margin.bottom;
    
        // 堆疊圖結構色票
        var colors = ["#FFFFFF", "#2AB3BC"];
        // 建立 svg 畫布
        var svg = d3
            .select("body")
            .select("#section3 .d_chart")
            .append("svg") 
            .attr("width", svgSize.width)
            .attr("height", svgSize.height)
        // 建立圖表群組
        var chart = svg
            .append("g")
            .attr("transform",`translate(${margin.left},${margin.top})`)
            .attr("class","pd_data_chart2");
    
        d3.json("../data/data.json")
          .then(data => {
            let n_data=data["section3_2"];

            const hourArray = ["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23",];
            const weekArray = ["星期日", "星期六", "星期五", "星期四", "星期三", "星期三", "星期二", "星期一"];
            
            const xScale = d3.scaleBand()
                        .domain(hourArray)
                        .range([ 0, width ])
                        .padding(0.01);

            const yScale = d3.scaleBand()
                        .range([ height, 0])
                        .domain(weekArray)
                        .padding(0.01);
            var axisX = d3.axisBottom(xScale)
                        // .tickSize(0)
                        .tickPadding(10)
            var axisY = d3.axisLeft(yScale)
                        .tickPadding(8)
                        .tickSize(0);

            chart.append("g")
                 .attr("transform", `translate(-1, ${height})`)
                 .call(axisX)
            chart.append("g")
                 .attr("transform", `translate(-1, 0)`)
                 .call(axisY);

        // Build color scale
        const myColor = d3.scaleLinear()
            .range(["#EDFEFF", "#38A6AD"])
            .domain([0,d3.max(n_data,d=>d.value)])

        d3.json("./data/data.json")
        .then(data=>{

            let n_data=data["test"];
            // console.log(n_data);

            chart.append("text")
                .attr("y", 285)
                .attr("x", width+15)
                .text("小時");
            chart.append("text")
                .attr("x", "-10px")
                .attr("y", "-20px")
                .attr("text-anchor", "end")
                .text("星期");

            chart.selectAll()
                .data(n_data, function(d) {
                    return d.group+':'+d.variable;})
                .join("rect")
                .attr("x", function(d) { return xScale(d.hour) })
                .attr("y", function(d) { return yScale(d.week) })
                .attr("width", xScale.bandwidth() )
                .attr("height", yScale.bandwidth() )
                .style("fill", function(d) { return myColor(d.value)} )
        })      
          })
          .catch(error => {
            console.log(error);
          });
        }
    // 初始化
    section2(); 
    section3_1();
    // 

    // 切換圖表按鈕
    $("#chart_btn button").on("click",(e)=>{
        $("#section3 .d_chart svg").remove();
        $("#chart_btn button").removeClass();
        let btn_id = e.target.id;
        if(btn_id == "chart_btn1"){
            $("#chart_btn1").attr("class","chart_btn_s")
            section3_1();
            
            $(".scale > img").attr("src","../pd_data/img/img_scale1.svg");
        }else if(btn_id == "chart_btn2"){
            $("#chart_btn2").attr("class","chart_btn_s")
            section3_2();
            $(".scale > img").attr("src","../pd_data/img/img_scale2.svg");
        }
    })
    // 二級選單 hover
    $(".d_nav_item").mouseover((e)=>{

        if(!$(`#${e.target.id}`).hasClass('d_nav_s')){
            $(`#${e.target.id}`).addClass("d_nav_h");
        }

        let index=(e.target.id.slice(3,4))

        // 輸出選項
        if(index != 0){
            $("#selection_box").append("<ul></ul>")
            $("#selection_box").css("visibility","visible");
            for(let i=0;i<l2_items[index].length;i++){
                // l2_1_1
                $("#selection_box ul").append(`<li id="l2_${index}_${i}">${l2_items[index][i]}</li>`)
            }
        }
        $("#selection_box").css("left",100*index+30);
    })
    $("#selection_box").hover(()=>{
        if(!$("#selection_box").is(":hover")){
            $("#selection_box ul").remove();
            $("#selection_box").css("visibility","hidden");
            $(".d_nav_item").removeClass("d_nav_h");
        }
    })
    $("#d_nav ul").mouseout(()=>{
        if(!$("#selection_box").is(":hover")){
            $("#selection_box ul").remove();
            $("#selection_box").css("visibility","hidden");
            $(".d_nav_item").removeClass("d_nav_h");
        }
    })
    // 二級選單點擊功能
    $("#selection_box").click((e)=>{
        let id =e.target.id;
        console.log($(`#${id.slice(0,4)}`).html());
        $(".d_nav_item").removeClass("d_nav_s");
        $(`#${id.slice(0,4)}`).attr("class","d_nav_s d_nav_item");
        $("#selection_box").css("visibility","hidden");
        $(".d_nav_item").removeClass("d_nav_h");

        $("#span1").html($(`#${id.slice(0,4)}`).html());
        $("#span2").html(e.target.innerHTML);
    })
    // 總覽點擊功能
    $("#l2_0").click((e)=>{
        $(".d_nav_item").removeClass("d_nav_s");
        $(`#l2_0`).attr("class","d_nav_s d_nav_item");
        $("#selection_box").css("visibility","hidden");
        $("#span1").html("總覽");
        $("#span2").html("");
    })
})