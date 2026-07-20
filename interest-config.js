/**
 * MapNoteHK interest form configuration.
 *
 * Where submissions go:
 * - FORM_ENDPOINT set → POST JSON to that URL (Formspree, Tally webhook, or your API).
 * - FORM_ENDPOINT empty → saved only in the visitor's browser localStorage (preview/dev).
 *
 * This is NOT Google Forms unless you paste a Google Apps Script or Formspree URL here.
 * You (the site owner) will NOT receive emails until FORM_ENDPOINT is configured.
 */
window.MapNoteInterestConfig = {
  /**
   * Remote submit URL. Examples:
   * - Formspree: 'https://formspree.io/f/xxxxxxxx'
   * - Custom API: 'https://your-server.com/api/interest'
   * Leave '' for local-only storage during static preview.
   */
  FORM_ENDPOINT: '',
  /** localStorage key when FORM_ENDPOINT is not set */
  STORAGE_KEY: 'mapnotehk_interest_submissions',
};
