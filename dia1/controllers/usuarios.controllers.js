import bcrypt from "bcryptjs";
import  jwt  from "jsonwebtoken";

const usuarios = [];

export const registroUsuario = async (req, res) => {
  // {'nombre': 'eduardo', 'apellido': 'de rivero', 'correo': 'ederiveroman@gmail.com', 'password':'Welcome123'}
  const data = req.body;
  const passwordHashed = bcrypt.hashSync(data.password, 10);
  console.log(passwordHashed);

  usuarios.push({ ...data, password: passwordHashed });

  return res
    .json({
      message: "Usuario creado exitosamente",
    })
    .status(201);
};

export const login =async (req,res)=>{
    const data =req.body;

    const usuarioEncontrado=usuarios.find(
        (usuario)=>usuario.correo===data.correo
    );
    if (!usuarioEncontrado){
        return res.status(404).json({
            message:"usuario no existe",
        });
    }
    const resultado =bcrypt.compareSync(
        data.password,
        usuarioEncontrado.password

    );

    if (resultado){

        const payload={
            correo:usuarioEncontrado.correo,
            mensaje:'hola',
        }
        const token=jwt.sign(payload,"ultramegasupersecreto",{
            expiresIn:"1h",
        })
        return res.json({
            message:"Bienvenido",
            content:token,
        });
    }   else{
        return res.status(403).json({
            message:"Usuariono existe",
        });
    }

};