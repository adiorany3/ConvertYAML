# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 25
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 31

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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-81MS` (url=218ms, nekobox=248ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-92MS` (url=236ms, nekobox=282ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-95MS` (url=205ms, nekobox=241ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-92MS` (url=234ms, nekobox=263ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-107MS` (url=206ms, nekobox=258ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-95MS` (url=224ms, nekobox=262ms, status=yes)
7. `AKUN-007-ZVC-VLESS-WS-107MS` (url=228ms, nekobox=264ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-98MS` (url=211ms, nekobox=241ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-115MS` (url=209ms, nekobox=261ms, status=yes)
10. `AKUN-010-WPENG-VLESS-WS-88MS` (url=275ms, nekobox=252ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-113MS` (url=235ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-107MS` (url=204ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-98MS` (url=203ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-97MS` (url=201ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-76MS` (url=294ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-108MS` (url=215ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-102MS` (url=222ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-104MS` (url=210ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-118MS` (url=202ms, status=HTTP 204)
20. `AKUN-022-POLICE-VLESS-WS-158MS` (url=228ms, status=HTTP 204)
21. `AKUN-025-UNKNOWN-VLESS-WS-264MS` (url=530ms, status=HTTP 204)
22. `AKUN-026-UNKNOWN-VLESS-WS-256MS` (url=578ms, status=HTTP 204)
23. `AKUN-027-CLOUDFLARE-VLESS-WS-270MS` (url=503ms, status=HTTP 204)
24. `AKUN-028-CLOUDFLARE-VLESS-WS-253MS` (url=513ms, status=HTTP 204)
25. `AKUN-029-CLOUDFLARE-VLESS-WS-277MS` (url=728ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
