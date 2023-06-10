 while Ingresar == True :
                        Preguntar = input (" ¿Desea Ingresar más productos s/n  ")
                        if Preguntar == "s" or Preguntar == "S" :
                            nProd = input("Ingrese el producto que desea comprar: ")
        
                            for z in Productos:
                                if nProd == z:
                                    cantidadProd = int(input("Ingrese cantidad: "))
                                    Compra[nProd] = cantidadProd * Productos[nProd]
                                    print("su compra")
                                    print(Compra)
                                else:
                                    pass
                else:
                    for b in Productos:
                        if nProd == z:
                            cantidadProd = int(input("Ingrese cantidad: "))
                            Compra[nProd] = cantidadProd * Productos[nProd]
                            print("su compra")
                            print(Compra)
                        time.sleep(3)
                        os.system("cls")
                        pass
                        elif(Preguntar.lower()=="n"):
                            Ingresar = False
                            MenuCaja()