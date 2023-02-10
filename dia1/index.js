const express=require ('express');


//const prisma = new PrismaCliente
//se va copiar toda la funcionalidad de la librerioa en la variable sevridor
const servidor =express ();
//que ahora mi servidor podra convertir la informacion entrante para los JSON
//middleware para convertir la informacion entrante a un formato legible
servidor.use(express.json());

//servidor.use(express.urlencoderd())

servidor.get('/',(req,res)=>{
    //req> es la informacion que me envia el cliente
    //resp> es la informacion que voy a devolver la cliente
    res.json({
        message:"Bienvenido a mi API",
    });
});

servidor.post('/productos', (req,res)=>{
    console.log(req.body);
    res.json({
        message:"Producto creado exitosamente",
    });
});

servidor.listen(5000,()=> {
    console.log('Servidor corriendo exitosamente en el puerto 5000');
});