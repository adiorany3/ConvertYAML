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
- Proxy di openclash_fresh_pool.yaml: 25

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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-62MS` (url=208ms, nekobox=238ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-80MS` (url=224ms, nekobox=230ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-88MS` (url=213ms, nekobox=254ms, status=yes)
4. `AKUN-004-ADF-VLESS-WS-82MS` (url=219ms, nekobox=233ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-81MS` (url=228ms, nekobox=240ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-99MS` (url=212ms, nekobox=248ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-119MS` (url=205ms, nekobox=230ms, status=yes)
8. `AKUN-008-VULTR-VLESS-WS-90MS` (url=213ms, nekobox=232ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-236MS` (url=486ms, nekobox=515ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-262MS` (url=578ms, nekobox=574ms, status=yes)
11. `AKUN-012-CLOUDFLARE-VLESS-WS-266MS` (url=557ms, status=HTTP 204)
12. `AKUN-013-CLOUDFLARE-VLESS-WS-253MS` (url=541ms, status=HTTP 204)
13. `AKUN-014-CLOUDFLARE-VLESS-WS-251MS` (url=551ms, status=HTTP 204)
14. `AKUN-019-UNKNOWN-VLESS-WS-426MS` (url=756ms, status=HTTP 204)
15. `AKUN-021-CLOUDFLARE-VLESS-WS-222MS` (url=483ms, status=HTTP 204)
16. `AKUN-024-CLOUDFLARE-VLESS-WS-234MS` (url=492ms, status=HTTP 204)
17. `AKUN-026-CLOUDFLARE-VLESS-WS-506MS` (url=806ms, status=HTTP 204)
18. `AKUN-028-CLOUDFLARE-VLESS-WS-170MS` (url=374ms, status=HTTP 204)
19. `AKUN-031-CLOUDFLARE-VLESS-WS-567MS` (url=857ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
