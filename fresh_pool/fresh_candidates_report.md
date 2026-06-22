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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-65MS` (url=239ms, nekobox=198ms, status=no)
2. `AKUN-001-VULTR-VLESS-WS-66MS`
3. `AKUN-002-CLOUDFLARE-VLESS-WS-71MS`
4. `AKUN-003-RS-RAPIDSEEDBOX-20190717-VLESS-WS-64MS`
5. `AKUN-004-CLOUDFLARE-VLESS-WS-87MS`
6. `AKUN-005-UNKNOWN-VLESS-WS-68MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-88MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-90MS`
9. `AKUN-008-UNKNOWN-VLESS-WS-91MS`
10. `AKUN-010-CLOUDFLARE-VLESS-WS-107MS` (url=228ms, nekobox=7178ms, status=no)
11. `AKUN-009-CLOUDFLARE-VLESS-WS-106MS`
12. `AKUN-010-UNKNOWN-VLESS-WS-98MS`
13. `AKUN-013-CLOUDFLARE-VLESS-WS-90MS` (url=202ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-119MS` (url=223ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-114MS` (url=240ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-346MS` (url=753ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-369MS` (url=779ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-391MS` (url=809ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-343MS` (url=755ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-405MS` (url=881ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-393MS` (url=823ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-397MS` (url=870ms, status=HTTP 204)
23. `AKUN-025-CLOUDFLARE-VLESS-WS-694MS` (url=948ms, status=HTTP 204)
24. `AKUN-031-CLOUDFLARE-VLESS-WS-743MS` (url=1193ms, status=HTTP 204)
25. `AKUN-033-CLOUDFLARE-VLESS-WS-802MS` (url=1294ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
