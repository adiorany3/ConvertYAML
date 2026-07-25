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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-71MS` (url=272ms, nekobox=307ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-78MS` (url=272ms, nekobox=338ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-75MS` (url=357ms, nekobox=304ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-76MS` (url=276ms, nekobox=345ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-81MS` (url=274ms, nekobox=307ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-82MS` (url=315ms, nekobox=345ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-84MS` (url=315ms, nekobox=374ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-80MS` (url=478ms, nekobox=321ms, status=yes)
9. `AKUN-009-DEV-VLESS-WS-80MS` (url=275ms, nekobox=305ms, status=yes)
10. `AKUN-010-UNKNOWN-VLESS-WS-75MS` (url=341ms, nekobox=370ms, status=yes)
11. `AKUN-011-UNKNOWN-VLESS-WS-76MS` (url=313ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-89MS` (url=343ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-119MS` (url=343ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-127MS` (url=381ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-179MS` (url=431ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-135MS` (url=354ms, status=HTTP 204)
17. `AKUN-017-DEV-VLESS-WS-76MS` (url=311ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-79MS` (url=315ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-80MS` (url=260ms, status=HTTP 204)
20. `AKUN-020-ZOOM-VLESS-WS-81MS` (url=344ms, status=HTTP 204)
21. `AKUN-021-008500-VLESS-WS-80MS` (url=360ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-113MS` (url=308ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-298MS` (url=574ms, status=HTTP 204)
24. `AKUN-024-LEVIKOGJGFDD-VLESS-WS-314MS` (url=707ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-77MS` (url=341ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
