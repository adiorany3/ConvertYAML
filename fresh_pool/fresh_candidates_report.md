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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-62MS` (url=209ms, nekobox=244ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-61MS` (url=208ms, nekobox=243ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-69MS` (url=220ms, nekobox=242ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-61MS` (url=195ms, nekobox=238ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-67MS` (url=221ms, nekobox=245ms, status=yes)
6. `AKUN-006-DEV-VLESS-WS-67MS` (url=219ms, nekobox=218ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-72MS` (url=195ms, nekobox=7173ms, status=no)
8. `AKUN-007-CLOUDFLARE-VLESS-WS-70MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-74MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-63MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-72MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-88MS` (url=192ms, status=HTTP 204)
13. `AKUN-013-DIXONS-VLESS-WS-92MS` (url=218ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-68MS` (url=224ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-98MS` (url=266ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-106MS` (url=217ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-65MS` (url=219ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-61MS` (url=228ms, status=HTTP 204)
19. `AKUN-019-102-177-176-0-102-177-17-VLESS-WS-71MS` (url=220ms, status=HTTP 204)
20. `AKUN-020-RS-RAPIDSEEDBOX-20190717-VLESS-WS-85MS` (url=207ms, status=HTTP 204)
21. `AKUN-021-RTCOMM-SRAVNI-RU-VLESS-WS-83MS` (url=226ms, status=HTTP 204)
22. `AKUN-022-UK-GB-DCL-01-20191003-VLESS-WS-110MS` (url=204ms, status=HTTP 204)
23. `AKUN-023-UK-GB-DCL-01-20191003-VLESS-WS-116MS` (url=226ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-109MS` (url=223ms, status=HTTP 204)
25. `AKUN-025-ZOOM-VLESS-WS-105MS` (url=218ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
