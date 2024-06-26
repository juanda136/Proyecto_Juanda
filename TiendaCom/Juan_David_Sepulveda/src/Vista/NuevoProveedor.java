/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/GUIForms/JFrame.java to edit this template
 */
package Vista;

import com.toedter.calendar.JDateChooser;
import javax.swing.JButton;
import javax.swing.JComboBox;
import javax.swing.JLabel;
import javax.swing.JTextField;

/**
 *
 * @author JUAN DAVID SEPULVEDA
 */
public class NuevoProveedor extends javax.swing.JFrame {

    /**
     * Creates new form NuevoUsuario1
     */
    public NuevoProveedor() {
        initComponents();
    }

    public JButton getBtnCancelar() {
        return BtnCancelar;
    }

    public JLabel getjLabelNuevoProveedor() {
        return jLabelNuevoProveedor;
    }

    public void setjLabelNuevoProveedor(JLabel jLabelNuevoProveedor) {
        this.jLabelNuevoProveedor = jLabelNuevoProveedor;
    }

    public void setBtnCancelar(JButton BtnCancelar) {
        this.BtnCancelar = BtnCancelar;
    }

    public JButton getBtnGuardarProveedor() {
        return BtnGuardarProveedor;
    }

    public void setBtnGuardarProveedor(JButton BtnGuardarProveedor) {
        this.BtnGuardarProveedor = BtnGuardarProveedor;
    }

    public JComboBox<String> getCbxSexo() {
        return cbxSexo;
    }

    public void setCbxSexo(JComboBox<String> cbxSexo) {
        this.cbxSexo = cbxSexo;
    }

    public JComboBox<String> getCbxTipoDocumento() {
        return cbxTipoDocumento;
    }

    public void setCbxTipoDocumento(JComboBox<String> cbxTipoDocumento) {
        this.cbxTipoDocumento = cbxTipoDocumento;
    }

    public JComboBox<String> getCbxTipoPersona() {
        return cbxTipoPersona;
    }

    public void setCbxTipoPersona(JComboBox<String> cbxTipoPersona) {
        this.cbxTipoPersona = cbxTipoPersona;
    }

    public JTextField getjTexCorreo() {
        return jTexCorreo;
    }

    public void setjTexCorreo(JTextField jTexCorreo) {
        this.jTexCorreo = jTexCorreo;
    }

    public JTextField getjTexDireccion() {
        return jTexDireccion;
    }

    public void setjTexDireccion(JTextField jTexDireccion) {
        this.jTexDireccion = jTexDireccion;
    }

    public JTextField getjTexNombre() {
        return jTexNombre;
    }

    public void setjTexNombre(JTextField jTexNombre) {
        this.jTexNombre = jTexNombre;
    }

    public JTextField getjTexTelefono() {
        return jTexTelefono;
    }

    public void setjTexTelefono(JTextField jTexTelefono) {
        this.jTexTelefono = jTexTelefono;
    }

    public JDateChooser getJdchFechaNacimiento() {
        return JdchFechaNacimiento;
    }

    public void setJdchFechaNacimiento(JDateChooser JdchFechaNacimiento) {
        this.JdchFechaNacimiento = JdchFechaNacimiento;
    }

    public JTextField getjTexDocumento() {
        return jTexDocumento;
    }

    public void setjTexDocumento(JTextField jTexDocumento) {
        this.jTexDocumento = jTexDocumento;
    }

    /**
     * This method is called from within the constructor to initialize the form.
     * WARNING: Do NOT modify this code. The content of this method is always
     * regenerated by the Form Editor.
     */
    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        cbxSexo = new javax.swing.JComboBox<>();
        jLabelTelefono = new javax.swing.JLabel();
        jTexTelefono = new javax.swing.JTextField();
        jLabel1 = new javax.swing.JLabel();
        jLabelnombre = new javax.swing.JLabel();
        jTexNombre = new javax.swing.JTextField();
        jLabel4 = new javax.swing.JLabel();
        BtnGuardarProveedor = new javax.swing.JButton();
        jTexCorreo = new javax.swing.JTextField();
        BtnCancelar = new javax.swing.JButton();
        jLabel5 = new javax.swing.JLabel();
        jLabelNuevoProveedor = new javax.swing.JLabel();
        jTexDireccion = new javax.swing.JTextField();
        jLabel7 = new javax.swing.JLabel();
        jLabel6 = new javax.swing.JLabel();
        JdchFechaNacimiento = new com.toedter.calendar.JDateChooser();
        cbxTipoDocumento = new javax.swing.JComboBox<>();
        jLabel3 = new javax.swing.JLabel();
        cbxTipoPersona = new javax.swing.JComboBox<>();
        jLabel2 = new javax.swing.JLabel();
        jTexDocumento = new javax.swing.JTextField();

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);

        jLabelTelefono.setText("Telefono");

        jLabel1.setText("Tipo de documento:");
        jLabel1.setToolTipText("");

        jLabelnombre.setText("Nombre");

        jLabel4.setText("Correo");

        BtnGuardarProveedor.setText("Guardar");
        BtnGuardarProveedor.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                BtnGuardarProveedorActionPerformed(evt);
            }
        });

        BtnCancelar.setText("Cancelar");

        jLabel5.setText("Direccion");

        jLabelNuevoProveedor.setText("NUEVO PROVEEDOR");

        jLabel7.setText("Fecha de Nacimiento");

        jLabel6.setText("sexo");

        JdchFechaNacimiento.setDateFormatString("yyyy-MM-dd");

        cbxTipoDocumento.setModel(new javax.swing.DefaultComboBoxModel<>(new String[] { "Seleccione:", "Tarjeta de identidad", "Pasaporte", "Cedula", "nit" }));

        jLabel3.setText("Tipo de Persona:");
        jLabel3.setToolTipText("");

        cbxTipoPersona.setModel(new javax.swing.DefaultComboBoxModel<>(new String[] { "Seleccione:", "Juridica", "Natural" }));

        jLabel2.setText("Documento :");

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, layout.createSequentialGroup()
                .addGap(0, 0, Short.MAX_VALUE)
                .addComponent(BtnGuardarProveedor)
                .addGap(83, 83, 83)
                .addComponent(BtnCancelar)
                .addGap(304, 304, 304))
            .addGroup(layout.createSequentialGroup()
                .addGap(40, 40, 40)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(layout.createSequentialGroup()
                        .addComponent(jLabel7)
                        .addGap(31, 31, 31)
                        .addComponent(JdchFechaNacimiento, javax.swing.GroupLayout.PREFERRED_SIZE, 220, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addGap(18, 18, 18)
                        .addComponent(jLabel3)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                        .addComponent(cbxTipoPersona, javax.swing.GroupLayout.PREFERRED_SIZE, 188, javax.swing.GroupLayout.PREFERRED_SIZE))
                    .addGroup(layout.createSequentialGroup()
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addComponent(jLabelnombre)
                            .addComponent(jLabel4)
                            .addComponent(jLabel5)
                            .addComponent(jLabel6)
                            .addComponent(jLabel2))
                        .addGap(30, 30, 30)
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addGroup(layout.createSequentialGroup()
                                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING, false)
                                    .addGroup(layout.createSequentialGroup()
                                        .addComponent(cbxSexo, javax.swing.GroupLayout.PREFERRED_SIZE, 206, javax.swing.GroupLayout.PREFERRED_SIZE)
                                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                                        .addComponent(jLabelTelefono))
                                    .addComponent(jTexDireccion, javax.swing.GroupLayout.PREFERRED_SIZE, 297, javax.swing.GroupLayout.PREFERRED_SIZE))
                                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                                    .addGroup(layout.createSequentialGroup()
                                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                                        .addComponent(jTexTelefono, javax.swing.GroupLayout.PREFERRED_SIZE, 155, javax.swing.GroupLayout.PREFERRED_SIZE))
                                    .addGroup(layout.createSequentialGroup()
                                        .addGap(23, 23, 23)
                                        .addComponent(jLabel1)
                                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                                        .addComponent(cbxTipoDocumento, javax.swing.GroupLayout.PREFERRED_SIZE, 188, javax.swing.GroupLayout.PREFERRED_SIZE))))
                            .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING, false)
                                .addComponent(jTexNombre)
                                .addComponent(jLabelNuevoProveedor)
                                .addComponent(jTexCorreo, javax.swing.GroupLayout.PREFERRED_SIZE, 448, javax.swing.GroupLayout.PREFERRED_SIZE))
                            .addComponent(jTexDocumento, javax.swing.GroupLayout.PREFERRED_SIZE, 463, javax.swing.GroupLayout.PREFERRED_SIZE))))
                .addContainerGap(47, Short.MAX_VALUE))
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addGap(14, 14, 14)
                .addComponent(jLabelNuevoProveedor)
                .addGap(18, 18, 18)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(jLabel2)
                    .addComponent(jTexDocumento, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addGap(18, 18, 18)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(jTexNombre, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(jLabelnombre, javax.swing.GroupLayout.PREFERRED_SIZE, 16, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addGap(26, 26, 26)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(jLabel4)
                    .addComponent(jTexCorreo, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addGap(22, 22, 22)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(jLabel5)
                    .addComponent(jTexDireccion, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(jLabel1)
                    .addComponent(cbxTipoDocumento, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addGap(27, 27, 27)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(jLabel6)
                    .addComponent(cbxSexo, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(jLabelTelefono)
                    .addComponent(jTexTelefono, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addGap(31, 31, 31)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addComponent(jLabel7)
                    .addComponent(JdchFechaNacimiento, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                        .addComponent(jLabel3)
                        .addComponent(cbxTipoPersona, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, 40, Short.MAX_VALUE)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(BtnCancelar)
                    .addComponent(BtnGuardarProveedor))
                .addGap(33, 33, 33))
        );

        pack();
    }// </editor-fold>//GEN-END:initComponents

    private void BtnGuardarProveedorActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_BtnGuardarProveedorActionPerformed

    }//GEN-LAST:event_BtnGuardarProveedorActionPerformed


    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JButton BtnCancelar;
    private javax.swing.JButton BtnGuardarProveedor;
    private com.toedter.calendar.JDateChooser JdchFechaNacimiento;
    private javax.swing.JComboBox<String> cbxSexo;
    private javax.swing.JComboBox<String> cbxTipoDocumento;
    private javax.swing.JComboBox<String> cbxTipoPersona;
    private javax.swing.JLabel jLabel1;
    private javax.swing.JLabel jLabel2;
    private javax.swing.JLabel jLabel3;
    private javax.swing.JLabel jLabel4;
    private javax.swing.JLabel jLabel5;
    private javax.swing.JLabel jLabel6;
    private javax.swing.JLabel jLabel7;
    private javax.swing.JLabel jLabelNuevoProveedor;
    private javax.swing.JLabel jLabelTelefono;
    private javax.swing.JLabel jLabelnombre;
    private javax.swing.JTextField jTexCorreo;
    private javax.swing.JTextField jTexDireccion;
    private javax.swing.JTextField jTexDocumento;
    private javax.swing.JTextField jTexNombre;
    private javax.swing.JTextField jTexTelefono;
    // End of variables declaration//GEN-END:variables
}