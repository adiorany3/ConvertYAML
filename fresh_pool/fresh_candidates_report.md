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
- Proxy di openclash_fresh_pool.yaml: 29

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
1. `AKUN-001-UNKNOWN-VLESS-WS-73MS` (url=229ms, nekobox=251ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-71MS` (url=222ms, nekobox=256ms, status=yes)
3. `AKUN-003-VULTR-VLESS-WS-73MS` (url=221ms, nekobox=257ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-75MS` (url=223ms, nekobox=252ms, status=yes)
5. `AKUN-005-ORG-VLESS-WS-82MS` (url=212ms, nekobox=260ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-80MS` (url=222ms, nekobox=246ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-70MS` (url=220ms, nekobox=244ms, status=yes)
8. `AKUN-008-ZVC-VLESS-WS-74MS` (url=220ms, nekobox=232ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-93MS` (url=239ms, nekobox=202ms, status=no)
10. `AKUN-009-CLOUDFLARE-VLESS-WS-89MS`
11. `AKUN-010-UNKNOWN-VLESS-WS-93MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-89MS` (url=239ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-106MS` (url=218ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-102MS` (url=228ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-79MS` (url=231ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-93MS` (url=232ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-99MS` (url=209ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-124MS` (url=206ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-105MS` (url=208ms, status=HTTP 204)
20. `AKUN-021-SKK-VLESS-WS-133MS` (url=290ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-144MS` (url=338ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-160MS` (url=292ms, status=HTTP 204)
23. `AKUN-024-UNKNOWN-VLESS-WS-186MS` (url=363ms, status=HTTP 204)
24. `AKUN-025-RMGYVPN-VLESS-WS-237MS` (url=562ms, status=HTTP 204)
25. `AKUN-026-UNKNOWN-VLESS-WS-338MS` (url=776ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
