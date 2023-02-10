const express=require ('express');

//se va copiar toda la funcionalidad de la librerioa en la variable sevridor
const servidor =express ();

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