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
- Proxy di openclash_fresh_pool.yaml: 30

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
1. `AKUN-001-ZVC-VLESS-WS-62MS` (url=211ms, nekobox=241ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-64MS` (url=534ms, nekobox=233ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-66MS` (url=207ms, nekobox=247ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-70MS` (url=209ms, nekobox=244ms, status=yes)
5. `AKUN-005-UK-GB-DCL-01-20191003-VLESS-WS-75MS` (url=232ms, nekobox=252ms, status=yes)
6. `AKUN-006-466688-VLESS-WS-63MS` (url=226ms, nekobox=241ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-66MS` (url=209ms, nekobox=234ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-71MS` (url=198ms, nekobox=7177ms, status=no)
9. `AKUN-008-CLOUDFLARE-VLESS-WS-82MS`
10. `AKUN-009-GO-DADDY-COM-LLC-VLESS-WS-85MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-84MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-90MS` (url=202ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-71MS` (url=224ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-76MS` (url=239ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-84MS` (url=235ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-90MS` (url=221ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-91MS` (url=234ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-96MS` (url=202ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-80MS` (url=216ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-102MS` (url=231ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-91MS` (url=222ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-105MS` (url=215ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-108MS` (url=212ms, status=HTTP 204)
24. `AKUN-024-WEBEX-VLESS-WS-71MS` (url=210ms, status=HTTP 204)
25. `AKUN-026-UNKNOWN-VLESS-WS-232MS` (url=525ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
