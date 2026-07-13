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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-62MS` (url=208ms, nekobox=243ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-70MS` (url=211ms, nekobox=236ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-73MS` (url=198ms, nekobox=233ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-76MS` (url=228ms, nekobox=309ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-67MS` (url=217ms, nekobox=234ms, status=yes)
6. `AKUN-006-ZVC-VLESS-WS-65MS` (url=202ms, nekobox=226ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-81MS` (url=207ms, nekobox=248ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-81MS` (url=198ms, nekobox=181ms, status=no)
9. `AKUN-008-CLOUDFLARE-VLESS-WS-83MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-109MS`
11. `AKUN-011-CLOUDFLARE-VLESS-WS-88MS` (url=224ms, nekobox=7176ms, status=no)
12. `AKUN-012-SPEEDTEST-VLESS-WS-132MS` (url=223ms, nekobox=183ms, status=no)
13. `AKUN-010-VOV-VLESS-WS-98MS`
14. `AKUN-014-466688-VLESS-WS-111MS` (url=216ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-81MS` (url=224ms, status=HTTP 204)
16. `AKUN-016-SPEEDTEST-VLESS-WS-105MS` (url=208ms, status=HTTP 204)
17. `AKUN-017-US-VLESS-WS-82MS` (url=225ms, status=HTTP 204)
18. `AKUN-018-VOV-VLESS-WS-107MS` (url=234ms, status=HTTP 204)
19. `AKUN-019-DEV-VLESS-WS-79MS` (url=221ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-94MS` (url=204ms, status=HTTP 204)
21. `AKUN-021-WEBEX-VLESS-WS-161MS` (url=206ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-96MS` (url=235ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-180MS` (url=212ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-229MS` (url=488ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-233MS` (url=524ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
