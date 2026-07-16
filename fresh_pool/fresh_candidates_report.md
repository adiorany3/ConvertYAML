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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-65MS` (url=219ms, nekobox=182ms, status=no)
2. `AKUN-001-CLOUDFLARE-VLESS-WS-62MS`
3. `AKUN-002-CLOUDFLARE-VLESS-WS-64MS`
4. `AKUN-003-RS-RAPIDSEEDBOX-20190717-VLESS-WS-72MS`
5. `AKUN-004-CLOUDFLARE-VLESS-WS-70MS`
6. `AKUN-005-CLOUDFLARE-VLESS-WS-60MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-66MS`
8. `AKUN-007-CZ-LOTUNA-19970206-VLESS-WS-79MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-58MS`
10. `AKUN-010-CLOUDFLARE-VLESS-WS-71MS` (url=223ms, nekobox=7176ms, status=no)
11. `AKUN-009-UNKNOWN-VLESS-WS-71MS`
12. `AKUN-010-466688-VLESS-WS-80MS`
13. `AKUN-013-UNKNOWN-VLESS-WS-87MS` (url=224ms, status=HTTP 204)
14. `AKUN-014-WEBEX-VLESS-WS-103MS` (url=223ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-75MS` (url=220ms, status=HTTP 204)
16. `AKUN-016-NEXUSMODS-VLESS-WS-100MS` (url=229ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-93MS` (url=209ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-77MS` (url=236ms, status=HTTP 204)
19. `AKUN-019-466688-VLESS-WS-119MS` (url=206ms, status=HTTP 204)
20. `AKUN-020-POLICE-VLESS-WS-94MS` (url=227ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-98MS` (url=222ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-92MS` (url=210ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-114MS` (url=210ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-109MS` (url=249ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-69MS` (url=223ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
