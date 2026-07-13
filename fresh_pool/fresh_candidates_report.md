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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-67MS` (url=218ms, nekobox=235ms, status=yes)
2. `AKUN-002-PUBLICDOMAINREGISTRY-NET-VLESS-WS-71MS` (url=194ms, nekobox=230ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-67MS` (url=218ms, nekobox=231ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-77MS` (url=202ms, nekobox=260ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-75MS` (url=200ms, nekobox=255ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-62MS` (url=200ms, nekobox=232ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-78MS` (url=201ms, nekobox=239ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-63MS` (url=223ms, nekobox=238ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-70MS` (url=203ms, nekobox=5157ms, status=no)
10. `AKUN-009-CLOUDFLARE-VLESS-WS-84MS`
11. `AKUN-010-466688-VLESS-WS-88MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-85MS` (url=218ms, status=HTTP 204)
13. `AKUN-013-IDC-SG-VLESS-WS-134MS` (url=232ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-119MS` (url=219ms, status=HTTP 204)
15. `AKUN-015-HETZNER-VLESS-WS-71MS` (url=237ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-80MS` (url=235ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-144MS` (url=223ms, status=HTTP 204)
18. `AKUN-018-HETZNER-VLESS-WS-135MS` (url=200ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-110MS` (url=225ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-225MS` (url=512ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-233MS` (url=701ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-239MS` (url=516ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-264MS` (url=548ms, status=HTTP 204)
24. `AKUN-026-CLOUDFLARE-VLESS-WS-435MS` (url=712ms, status=HTTP 204)
25. `AKUN-027-UNKNOWN-VLESS-WS-244MS` (url=517ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
