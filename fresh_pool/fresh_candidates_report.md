# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 24
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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-91MS` (url=261ms, nekobox=246ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-98MS` (url=221ms, nekobox=235ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-101MS` (url=214ms, nekobox=292ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-105MS` (url=219ms, nekobox=238ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-102MS` (url=207ms, nekobox=246ms, status=yes)
6. `AKUN-006-ZOOM-VLESS-WS-116MS` (url=218ms, nekobox=229ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-101MS` (url=207ms, nekobox=235ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-122MS` (url=224ms, nekobox=250ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-113MS` (url=211ms, nekobox=248ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-138MS` (url=243ms, nekobox=272ms, status=yes)
11. `AKUN-011-PUBLICDOMAINREGISTRY-NET-VLESS-WS-107MS` (url=244ms, status=HTTP 204)
12. `AKUN-013-CLOUDFLARE-VLESS-WS-215MS` (url=412ms, status=HTTP 204)
13. `AKUN-014-CLOUDFLARE-VLESS-WS-374MS` (url=4580ms, status=HTTP 204)
14. `AKUN-015-CLOUDFLARE-VLESS-WS-389MS` (url=816ms, status=HTTP 204)
15. `AKUN-016-CLOUDFLARE-VLESS-WS-366MS` (url=811ms, status=HTTP 204)
16. `AKUN-017-CLOUDFLARE-VLESS-WS-394MS` (url=832ms, status=HTTP 204)
17. `AKUN-018-UNKNOWN-VLESS-WS-387MS` (url=4221ms, status=HTTP 204)
18. `AKUN-019-UNKNOWN-VLESS-WS-413MS` (url=831ms, status=HTTP 204)
19. `AKUN-020-UNKNOWN-VLESS-WS-403MS` (url=517ms, status=HTTP 204)
20. `AKUN-021-DEV-VLESS-WS-446MS` (url=1201ms, status=HTTP 204)
21. `AKUN-027-CLOUDFLARE-VLESS-WS-275MS` (url=3159ms, status=HTTP 204)
22. `AKUN-030-RS-RAPIDSEEDBOX-20190717-VLESS-WS-750MS` (url=1146ms, status=HTTP 204)
23. `AKUN-032-UNKNOWN-VLESS-WS-748MS` (url=894ms, status=HTTP 204)
24. `AKUN-033-CLOUDFLARE-VLESS-WS-470MS` (url=913ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
