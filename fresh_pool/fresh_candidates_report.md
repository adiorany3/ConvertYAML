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
1. `AKUN-001-IONOS-VLESS-WS-59MS` (url=228ms, nekobox=242ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-63MS` (url=204ms, nekobox=253ms, status=yes)
3. `AKUN-003-ZVC-VLESS-WS-72MS` (url=198ms, nekobox=234ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-65MS` (url=203ms, nekobox=238ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-80MS` (url=229ms, nekobox=246ms, status=yes)
6. `AKUN-006-090227-VLESS-WS-81MS` (url=212ms, nekobox=249ms, status=yes)
7. `AKUN-007-PUBLICDOMAINREGISTRY-NET-VLESS-WS-79MS` (url=218ms, nekobox=230ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-87MS` (url=230ms, nekobox=249ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-93MS` (url=215ms, nekobox=246ms, status=yes)
10. `AKUN-010-UNKNOWN-VLESS-WS-70MS` (url=225ms, nekobox=241ms, status=yes)
11. `AKUN-011-UNKNOWN-VLESS-WS-96MS` (url=273ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-84MS` (url=208ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-105MS` (url=228ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-78MS` (url=212ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-126MS` (url=216ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-101MS` (url=220ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-116MS` (url=217ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-125MS` (url=198ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-97MS` (url=217ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-135MS` (url=205ms, status=HTTP 204)
21. `AKUN-021-INTERNETWORKS-45-131-210-VLESS-WS-228MS` (url=681ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-233MS` (url=527ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-242MS` (url=2475ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-246MS` (url=541ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-258MS` (url=537ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
