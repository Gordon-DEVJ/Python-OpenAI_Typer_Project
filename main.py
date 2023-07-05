import openai 
import config
import typer
from rich import print
from rich.table import Table

#inicio del programa
def main():

    #llamada a la api_key
    openai.api_key = config.api_key

    #Mensaje inicial y tabla de comandos
    print("[bold red] OpenAI_ChatGPT Simple Project [/bold red]")
    table = Table("Comando", "Descricion")
    table.add_row("exit", "Salir")
    table.add_row("new", "Nueva conversacion")
    print(table)

    #contexto del asistente
    context= {"role": "system", 
              "content": "eres un asistente muy util"}
    messages = [context]

    #preguntar al asistente
    while True:

        content = __prompt()

        #Nueva conversacion
        if content == 'new':
            print ("[bold red]Nueva Conversacion[/bold red]")
            messages = [context]
            content = __prompt()

        messages.append({"role": "user", "content": content})

        #LLamada con la pregunta a la api
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages)

        #Unica respuesta
        response_content = response.choices[0].message.content

        messages.append({"role": "assistant", "content": response_content})

        #Respuesta para el usuario. 
        print (f"[bold red]>[/bold red] {response_content}") 

def __prompt()-> str: 
#se encargara de la salida del programa y de la pregunta al asistente.
    prompt = typer.prompt("\nQue pregunta tienes?")

    if prompt == "exit":
        exit = typer.confirm("Seguro?")
        if exit:
            print("[bold red]Adios[/bold red]")
            raise typer.Abort()
        return __prompt()
    return prompt

if __name__ == "__main__":
    typer.run(main)