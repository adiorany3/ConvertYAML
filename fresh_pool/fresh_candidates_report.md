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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-76MS` (url=229ms, nekobox=266ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-82MS` (url=236ms, nekobox=273ms, status=yes)
3. `AKUN-003-ZVC-VLESS-WS-101MS` (url=283ms, nekobox=279ms, status=yes)
4. `AKUN-004-RS-RAPIDSEEDBOX-20190717-VLESS-WS-108MS` (url=247ms, nekobox=262ms, status=yes)
5. `AKUN-005-COMPREND-NET-VLESS-WS-104MS` (url=253ms, nekobox=293ms, status=yes)
6. `AKUN-006-AEZA-NETWORK-VLESS-WS-134MS` (url=250ms, nekobox=283ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-97MS` (url=251ms, nekobox=188ms, status=no)
8. `AKUN-007-CLOUDFLARE-VLESS-WS-113MS`
9. `AKUN-008-RS-RAPIDSEEDBOX-20190717-VLESS-WS-125MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-78MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-84MS`
12. `AKUN-012-COMPREND-NET-VLESS-WS-167MS` (url=259ms, status=HTTP 204)
13. `AKUN-013-466688-VLESS-WS-234MS` (url=452ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-85MS` (url=243ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-92MS` (url=319ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-105MS` (url=274ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-280MS` (url=564ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-307MS` (url=643ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-271MS` (url=544ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-302MS` (url=657ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-318MS` (url=676ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-306MS` (url=465ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-279MS` (url=674ms, status=HTTP 204)
24. `AKUN-026-UNKNOWN-VLESS-WS-305MS` (url=658ms, status=HTTP 204)
25. `AKUN-029-RS-RAPIDSEEDBOX-20190717-VLESS-WS-557MS` (url=872ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
