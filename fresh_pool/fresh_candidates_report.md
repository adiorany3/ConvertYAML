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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-81MS` (url=294ms, nekobox=301ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-90MS` (url=321ms, nekobox=315ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-84MS` (url=272ms, nekobox=307ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-106MS` (url=343ms, nekobox=533ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-105MS` (url=377ms, nekobox=339ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-108MS` (url=320ms, nekobox=326ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-102MS` (url=289ms, nekobox=380ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-118MS` (url=296ms, nekobox=319ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-85MS` (url=366ms, nekobox=337ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-132MS` (url=298ms, nekobox=349ms, status=yes)
11. `AKUN-011-UNKNOWN-VLESS-WS-109MS` (url=292ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-140MS` (url=357ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-91MS` (url=309ms, status=HTTP 204)
14. `AKUN-014-090227-VLESS-WS-151MS` (url=401ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-178MS` (url=385ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-252MS` (url=495ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-186MS` (url=355ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-152MS` (url=446ms, status=HTTP 204)
19. `AKUN-019-SKK-VLESS-WS-278MS` (url=483ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-295MS` (url=649ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-295MS` (url=676ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-285MS` (url=595ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-409MS` (url=759ms, status=HTTP 204)
24. `AKUN-025-SUKARIO-VLESS-WS-508MS` (url=812ms, status=HTTP 204)
25. `AKUN-026-UNKNOWN-VLESS-WS-560MS` (url=916ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
