# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 21
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 27

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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-92MS` (url=254ms, nekobox=262ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-92MS` (url=216ms, nekobox=281ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-83MS` (url=221ms, nekobox=292ms, status=yes)
4. `AKUN-004-RS-RAPIDSEEDBOX-20190717-VLESS-WS-89MS` (url=271ms, nekobox=262ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-96MS` (url=209ms, nekobox=254ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-135MS` (url=207ms, nekobox=268ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-101MS` (url=236ms, nekobox=284ms, status=yes)
8. `AKUN-008-RS-RAPIDSEEDBOX-20190717-VLESS-WS-64MS` (url=223ms, nekobox=271ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-181MS` (url=231ms, nekobox=264ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-132MS` (url=226ms, nekobox=241ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-383MS` (url=872ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-406MS` (url=4659ms, status=HTTP 204)
13. `AKUN-013-CONFLU-VLESS-WS-384MS` (url=766ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-373MS` (url=722ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-414MS` (url=805ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-436MS` (url=914ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-396MS` (url=820ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-409MS` (url=2460ms, status=HTTP 204)
19. `AKUN-021-UNKNOWN-VLESS-WS-646MS` (url=3977ms, status=HTTP 204)
20. `AKUN-024-UNKNOWN-VLESS-WS-639MS` (url=876ms, status=HTTP 204)
21. `AKUN-026-UNKNOWN-VLESS-WS-682MS` (url=1054ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
