# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 11
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 17

## Cara Pakai di OpenWrt
Jalankan manual saat node mulai mati:

```sh
sh /etc/mihomo-autopilot/openwrt_pull_fresh_pool.sh
```

Atau aktifkan guard otomatis:

```sh
sh /etc/mihomo-autopilot/openwrt_fresh_guard.sh
```

## Kandidat Fresh Teratas
1. `AKUN-001-UNKNOWN-VLESS-WS-100MS` (url=239ms, nekobox=245ms, status=yes)
2. `AKUN-002-HCAPTCHA-VLESS-WS-102MS` (url=217ms, nekobox=215ms, status=no)
3. `AKUN-002-CLOUDFLARE-VLESS-WS-398MS`
4. `AKUN-003-CLOUDFLARE-VLESS-WS-441MS`
5. `AKUN-004-UNKNOWN-VLESS-WS-421MS`
6. `AKUN-005-RS-RAPIDSEEDBOX-20190717-VLESS-WS-108MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-394MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-484MS`
9. `AKUN-008-KAWAII520-VLESS-WS-673MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-872MS`
11. `AKUN-010-RS-RAPIDSEEDBOX-20190717-VLESS-WS-782MS`

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
