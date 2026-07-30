# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 19
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 23

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
1. `AKUN-001-GOOGLE-VLESS-WS-71MS` (url=219ms, nekobox=243ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-62MS` (url=219ms, nekobox=237ms, status=yes)
3. `AKUN-003-SEECK-VLESS-WS-65MS` (url=214ms, nekobox=227ms, status=yes)
4. `AKUN-004-ZOOM-VLESS-WS-57MS` (url=219ms, nekobox=235ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-101MS` (url=211ms, nekobox=236ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-93MS` (url=217ms, nekobox=249ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-67MS` (url=212ms, nekobox=237ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-92MS`
9. `AKUN-009-UNKNOWN-VLESS-WS-70MS`
10. `AKUN-010-CLOUDFLARE-VLESS-WS-98MS`
11. `AKUN-012-UNKNOWN-VLESS-WS-75MS` (url=233ms, status=HTTP 204)
12. `AKUN-013-CLOUDFLARE-VLESS-WS-75MS` (url=203ms, status=HTTP 204)
13. `AKUN-015-CLOUDFLARE-VLESS-WS-141MS` (url=211ms, status=HTTP 204)
14. `AKUN-018-CLOUDFLARE-VLESS-WS-351MS` (url=760ms, status=HTTP 204)
15. `AKUN-019-CLOUDFLARE-VLESS-WS-345MS` (url=5354ms, status=HTTP 204)
16. `AKUN-023-UNKNOWN-VLESS-WS-384MS` (url=2162ms, status=HTTP 204)
17. `AKUN-024-CLOUDFLARE-VLESS-WS-452MS` (url=957ms, status=HTTP 204)
18. `AKUN-026-CLOUDFLARE-VLESS-WS-59MS` (url=809ms, status=HTTP 204)
19. `AKUN-030-UNKNOWN-VLESS-WS-825MS` (url=1343ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
