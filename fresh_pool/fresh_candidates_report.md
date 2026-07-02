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
1. `AKUN-001-ORACLE-VLESS-WS-82MS` (url=250ms, nekobox=279ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-73MS` (url=236ms, nekobox=271ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-89MS` (url=293ms, nekobox=300ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-86MS` (url=291ms, nekobox=292ms, status=yes)
5. `AKUN-005-WPENG-VLESS-WS-98MS` (url=242ms, nekobox=270ms, status=yes)
6. `AKUN-006-COMPREND-NET-VLESS-WS-110MS` (url=304ms, nekobox=517ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-96MS` (url=279ms, nekobox=285ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-105MS` (url=246ms, nekobox=298ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-103MS` (url=268ms, nekobox=290ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-114MS` (url=243ms, nekobox=299ms, status=yes)
11. `AKUN-011-COMPREND-NET-VLESS-WS-86MS` (url=276ms, status=HTTP 204)
12. `AKUN-012-COMPREND-NET-VLESS-WS-109MS` (url=265ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-106MS` (url=271ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-95MS` (url=254ms, status=HTTP 204)
15. `AKUN-015-ZVC-VLESS-WS-89MS` (url=242ms, status=HTTP 204)
16. `AKUN-016-COMPREND-NET-VLESS-WS-135MS` (url=273ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-124MS` (url=254ms, status=HTTP 204)
18. `AKUN-018-RS-RAPIDSEEDBOX-20190717-VLESS-WS-136MS` (url=262ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-128MS` (url=265ms, status=HTTP 204)
20. `AKUN-020-WPENG-VLESS-WS-82MS` (url=283ms, status=HTTP 204)
21. `AKUN-021-COMPREND-NET-VLESS-WS-159MS` (url=230ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-254MS` (url=564ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-270MS` (url=596ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-283MS` (url=602ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-282MS` (url=620ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
