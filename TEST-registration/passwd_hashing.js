export async function sha256(message) {
    const msgBuffer = new TextEncoder().encode(message);
    const hashBuffer = await crypto.subtle.digest('SHA-256', msgBuffer);
    const hashHex = Array.from(new Uint8Array(hashBuffer)).reduce((str, byte) => str + byte.toString(16).padStart(2, '0'), '');
    return hashHex;
}
