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
1. `AKUN-001-UNKNOWN-VLESS-WS-69MS` (url=292ms, nekobox=307ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-72MS` (url=271ms, nekobox=301ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-75MS` (url=284ms, nekobox=293ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-86MS`
5. `AKUN-006-DEV-VLESS-WS-71MS` (url=285ms, nekobox=201ms, status=no)
6. `AKUN-005-GO-DADDY-COM-LLC-VLESS-WS-85MS`
7. `AKUN-008-CLOUDFLARE-VLESS-WS-74MS` (url=285ms, nekobox=186ms, status=no)
8. `AKUN-006-RS-RAPIDSEEDBOX-20190717-VLESS-WS-70MS`
9. `AKUN-010-CLOUDFLARE-VLESS-WS-96MS` (url=317ms, nekobox=184ms, status=no)
10. `AKUN-011-CLOUDFLARE-VLESS-WS-100MS` (url=289ms, nekobox=192ms, status=no)
11. `AKUN-007-CLOUDFLARE-VLESS-WS-112MS`
12. `AKUN-008-CLOUDFLARE-VLESS-WS-110MS`
13. `AKUN-014-CLOUDFLARE-VLESS-WS-81MS` (url=303ms, nekobox=193ms, status=no)
14. `AKUN-015-DEV-VLESS-WS-94MS` (url=302ms, nekobox=183ms, status=no)
15. `AKUN-017-DEV-VLESS-WS-110MS` (url=285ms, nekobox=182ms, status=no)
16. `AKUN-009-CLOUDFLARE-VLESS-WS-138MS`
17. `AKUN-020-CLOUDFLARE-VLESS-WS-100MS` (url=305ms, nekobox=200ms, status=no)
18. `AKUN-010-UNKNOWN-VLESS-WS-95MS`
19. `AKUN-022-UNKNOWN-VLESS-WS-125MS` (url=288ms, status=HTTP 204)
20. `AKUN-023-RS-RAPIDSEEDBOX-20190717-VLESS-WS-145MS` (url=272ms, status=HTTP 204)
21. `AKUN-024-UNKNOWN-VLESS-WS-188MS` (url=427ms, status=HTTP 204)
22. `AKUN-025-CLOUDFLARE-VLESS-WS-274MS` (url=566ms, status=HTTP 204)
23. `AKUN-026-UNKNOWN-VLESS-WS-279MS` (url=542ms, status=HTTP 204)
24. `AKUN-027-CLOUDFLARE-VLESS-WS-262MS` (url=612ms, status=HTTP 204)
25. `AKUN-028-CLOUDFLARE-VLESS-WS-291MS` (url=601ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
