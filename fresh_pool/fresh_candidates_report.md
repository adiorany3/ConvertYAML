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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-66MS` (url=230ms, nekobox=247ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-75MS` (url=219ms, nekobox=248ms, status=yes)
3. `AKUN-003-COMPREND-NET-VLESS-WS-80MS` (url=215ms, nekobox=258ms, status=yes)
4. `AKUN-004-COMPREND-NET-VLESS-WS-86MS` (url=222ms, nekobox=233ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-90MS` (url=213ms, nekobox=259ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-85MS` (url=228ms, nekobox=231ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-93MS` (url=218ms, nekobox=255ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-80MS` (url=224ms, nekobox=232ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-120MS` (url=221ms, nekobox=254ms, status=yes)
10. `AKUN-010-UNKNOWN-VLESS-WS-94MS` (url=235ms, nekobox=344ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-105MS` (url=234ms, status=HTTP 204)
12. `AKUN-012-RS-RAPIDSEEDBOX-20190717-VLESS-WS-110MS` (url=214ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-81MS` (url=223ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-70MS` (url=207ms, status=HTTP 204)
15. `AKUN-015-ZVC-VLESS-WS-123MS` (url=233ms, status=HTTP 204)
16. `AKUN-017-CONFLU-VLESS-WS-233MS` (url=497ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-271MS` (url=602ms, status=HTTP 204)
18. `AKUN-019-UNKNOWN-VLESS-WS-272MS` (url=494ms, status=HTTP 204)
19. `AKUN-020-UNKNOWN-VLESS-WS-279MS` (url=584ms, status=HTTP 204)
20. `AKUN-021-UNKNOWN-VLESS-WS-73MS` (url=214ms, status=HTTP 204)
21. `AKUN-022-UNKNOWN-VLESS-WS-260MS` (url=607ms, status=HTTP 204)
22. `AKUN-023-UNKNOWN-VLESS-WS-278MS` (url=589ms, status=HTTP 204)
23. `AKUN-024-COMPREND-NET-VLESS-WS-78MS` (url=236ms, status=HTTP 204)
24. `AKUN-025-UNKNOWN-VLESS-WS-93MS` (url=218ms, status=HTTP 204)
25. `AKUN-026-CLOUDFLARE-VLESS-WS-311MS` (url=4216ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
