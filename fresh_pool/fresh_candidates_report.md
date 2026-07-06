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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-68MS` (url=223ms, nekobox=251ms, status=yes)
2. `AKUN-002-ZVC-VLESS-WS-69MS` (url=251ms, nekobox=243ms, status=yes)
3. `AKUN-003-WEYRO-NET-VLESS-WS-79MS` (url=236ms, nekobox=263ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-89MS` (url=230ms, nekobox=245ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-91MS` (url=235ms, nekobox=234ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-69MS` (url=314ms, nekobox=263ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-94MS` (url=291ms, nekobox=263ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-82MS` (url=214ms, nekobox=251ms, status=yes)
9. `AKUN-009-DIGITALOCEAN-VLESS-WS-97MS` (url=227ms, nekobox=302ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-82MS` (url=242ms, nekobox=195ms, status=no)
11. `AKUN-010-WPENG-VLESS-WS-73MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-116MS` (url=232ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-76MS` (url=212ms, status=HTTP 204)
14. `AKUN-015-ZVC-VLESS-WS-114MS` (url=235ms, status=HTTP 204)
15. `AKUN-016-WPENG-VLESS-WS-99MS` (url=260ms, status=HTTP 204)
16. `AKUN-017-466688-VLESS-WS-121MS` (url=231ms, status=HTTP 204)
17. `AKUN-018-UNKNOWN-VLESS-WS-368MS` (url=758ms, status=HTTP 204)
18. `AKUN-019-UNKNOWN-VLESS-WS-376MS` (url=816ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-386MS` (url=787ms, status=HTTP 204)
20. `AKUN-021-UNKNOWN-VLESS-WS-369MS` (url=742ms, status=HTTP 204)
21. `AKUN-022-UNKNOWN-VLESS-WS-374MS` (url=838ms, status=HTTP 204)
22. `AKUN-023-UNKNOWN-VLESS-WS-386MS` (url=813ms, status=HTTP 204)
23. `AKUN-024-UNKNOWN-VLESS-WS-408MS` (url=826ms, status=HTTP 204)
24. `AKUN-025-UNKNOWN-VLESS-WS-636MS` (url=1080ms, status=HTTP 204)
25. `AKUN-026-UNKNOWN-VLESS-WS-697MS` (url=1109ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
