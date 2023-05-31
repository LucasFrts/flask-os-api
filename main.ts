declare namespace NodeJS {
    interface ProcessEnv {
      API_URL: string;
    }
}
class Rotas{
    public static getNextPage(){
        return '/getNextPageUrl'
    }
}
function sendUrlToScrapApplication(event:MouseEvent){
    event.preventDefault()
    console.log('teste')
    const target = event.target
    if(target instanceof HTMLAnchorElement){
        const apiUrl:string = process.env.API_URL 
        console.log(apiUrl)
        const link = target.href
        const request = {link:link}
        const requestOptions = {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
        },
        body: JSON.stringify(request),
        
        };
        const prox = (data:any)=>{
            console.log(data)
        }
        fetch(apiUrl + Rotas.getNextPage(), requestOptions)
        .then(response => response.json())
        .then(response => prox(response))
    }
}