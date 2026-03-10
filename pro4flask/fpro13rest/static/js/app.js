// 함수(화살표함수) 객체 생성 후 $에 할당

const $ = (sel) => document.querySelector(sel);
// 위와 동일한 의미
// function $(sel){
//     return document.querySelector(sel);
// }
// ex) $("#sendBtn") 하면 document.querySelector(sel)가 실행

$("#sendBtn").addEventListener("click", async() => {
    const name = $("#name").value.trim();
    const age = document.querySelector("#age").value.trim();

    const params = new URLSearchParams({name, age})     
    // 공백, 한글이 포함된 경우 자동 인코딩: 홍길동 -> %ED%78%....
    const url = `/api/friend?${params.toString()}`
    // 최종 URL 생성 : `/api/friend?name=%ED%78%....

    $("#result").textContent = "요청 중...";   
    // 서버에 자료 요청 시간이 길어지면 보이는 메시지

    try{
        const res = await fetch(url,{
            method: "GET",
            headers:{"Accept":"application/json"}   // mime type
        });
        
        const data = await res.json();  // 응답 본문을 JSON으로 파싱해서 JS객체화

        if(!res.ok || data.ok ===false){
            $("#result").innerHTML = 
                `<span class="error"> 에러 : ${data.error}</span>`
            return;    
        }

        // 요청 성공인 경우
        $("#result").innerHTML = `
            <div>이름 : ${data.name}</div>
            <div>나이 : ${data.age}</div>
            <div>연령대 : ${data.age_group}</div>
            <div>메세지 : ${data.message}</div>
            `

    }catch(err){
        $("#result").innerHTML = `<span class="error">네트워크, 파싱 오류 : ${err}</span>`
    }
});
