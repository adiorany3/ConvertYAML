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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-59MS` (url=210ms, nekobox=249ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-61MS` (url=222ms, nekobox=262ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-66MS` (url=229ms, nekobox=179ms, status=no)
4. `AKUN-003-UNKNOWN-VLESS-WS-67MS`
5. `AKUN-004-CLOUDFLARE-VLESS-WS-68MS`
6. `AKUN-005-CLOUDFLARE-VLESS-WS-61MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-67MS`
8. `AKUN-007-DEV-VLESS-WS-62MS`
9. `AKUN-008-DIGITALOCEAN-VLESS-WS-72MS`
10. `AKUN-009-MEDIUM-VLESS-WS-75MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-93MS`
12. `AKUN-012-UNKNOWN-VLESS-WS-101MS` (url=216ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-58MS` (url=212ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-100MS` (url=218ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-86MS` (url=199ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-61MS` (url=214ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-65MS` (url=228ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-62MS` (url=223ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-76MS` (url=219ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-73MS` (url=231ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-65MS` (url=220ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-116MS` (url=251ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-62MS` (url=216ms, status=HTTP 204)
24. `AKUN-024-DEV-VLESS-WS-65MS` (url=218ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-58MS` (url=211ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
