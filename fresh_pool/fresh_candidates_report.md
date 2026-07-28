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
1. `AKUN-001-UNKNOWN-VLESS-WS-55MS` (url=206ms, nekobox=232ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-56MS` (url=212ms, nekobox=239ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-57MS` (url=211ms, nekobox=238ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-65MS` (url=212ms, nekobox=240ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-61MS` (url=205ms, nekobox=233ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-62MS` (url=216ms, nekobox=248ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-65MS` (url=222ms, nekobox=244ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-59MS` (url=216ms, nekobox=234ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-57MS` (url=210ms, nekobox=245ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-62MS` (url=227ms, nekobox=244ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-69MS` (url=332ms, status=HTTP 204)
12. `AKUN-012-SPEEDTEST-VLESS-WS-62MS` (url=229ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-84MS` (url=208ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-60MS` (url=210ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-94MS` (url=209ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-87MS` (url=206ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-58MS` (url=213ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-110MS` (url=207ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-124MS` (url=237ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-61MS` (url=214ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-71MS` (url=217ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-59MS` (url=215ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-66MS` (url=215ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-326MS` (url=730ms, status=HTTP 204)
25. `AKUN-026-CLOUDFLARE-VLESS-WS-65MS` (url=216ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
