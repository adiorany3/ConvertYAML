# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 22
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 28

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
1. `AKUN-001-UNKNOWN-VLESS-WS-96MS` (url=259ms, nekobox=274ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-90MS` (url=257ms, nekobox=187ms, status=no)
3. `AKUN-003-DEV-VLESS-WS-112MS` (url=258ms, nekobox=190ms, status=no)
4. `AKUN-002-CLOUDFLARE-VLESS-WS-89MS`
5. `AKUN-003-RS-RAPIDSEEDBOX-20190717-VLESS-WS-112MS`
6. `AKUN-004-UNKNOWN-VLESS-WS-99MS`
7. `AKUN-005-CLOUDFLARE-VLESS-WS-79MS`
8. `AKUN-006-CLOUDFLARE-VLESS-WS-124MS`
9. `AKUN-007-CLOUDFLARE-VLESS-WS-141MS`
10. `AKUN-008-CLOUDFLARE-VLESS-WS-108MS`
11. `AKUN-009-CLOUDFLARE-VLESS-WS-166MS`
12. `AKUN-012-DEV-VLESS-WS-112MS` (url=309ms, nekobox=188ms, status=no)
13. `AKUN-010-CONFLU-VLESS-WS-280MS`
14. `AKUN-015-CLOUDFLARE-VLESS-WS-271MS` (url=604ms, status=HTTP 204)
15. `AKUN-016-CLOUDFLARE-VLESS-WS-319MS` (url=2848ms, status=HTTP 204)
16. `AKUN-018-CLOUDFLARE-VLESS-WS-319MS` (url=3266ms, status=HTTP 204)
17. `AKUN-020-CLOUDFLARE-VLESS-WS-294MS` (url=662ms, status=HTTP 204)
18. `AKUN-021-CLOUDFLARE-VLESS-WS-308MS` (url=635ms, status=HTTP 204)
19. `AKUN-023-CLOUDFLARE-VLESS-WS-322MS` (url=639ms, status=HTTP 204)
20. `AKUN-027-CLOUDFLARE-VLESS-WS-445MS` (url=734ms, status=HTTP 204)
21. `AKUN-029-CLOUDFLARE-VLESS-WS-448MS` (url=657ms, status=HTTP 204)
22. `AKUN-034-BIGCOMMERCE-VLESS-WS-489MS` (url=815ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
