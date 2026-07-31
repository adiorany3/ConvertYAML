# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 21
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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-61MS` (url=207ms, nekobox=240ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-62MS` (url=198ms, nekobox=236ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-59MS` (url=215ms, nekobox=226ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-60MS` (url=198ms, nekobox=236ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-85MS` (url=212ms, nekobox=238ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-93MS` (url=225ms, nekobox=248ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-109MS` (url=203ms, nekobox=239ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-69MS` (url=214ms, nekobox=312ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-82MS` (url=200ms, nekobox=228ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-90MS` (url=197ms, nekobox=233ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-116MS` (url=224ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-179MS` (url=351ms, status=HTTP 204)
13. `AKUN-015-TW-CLOUD-VLESS-WS-259MS` (url=735ms, status=HTTP 204)
14. `AKUN-019-CLOUDFLARE-VLESS-WS-433MS` (url=767ms, status=HTTP 204)
15. `AKUN-021-CLOUDFLARE-VLESS-WS-408MS` (url=713ms, status=HTTP 204)
16. `AKUN-022-CLOUDFLARE-VLESS-WS-424MS` (url=655ms, status=HTTP 204)
17. `AKUN-025-CLOUDFLARE-VLESS-WS-463MS` (url=814ms, status=HTTP 204)
18. `AKUN-028-CLOUDFLARE-VLESS-WS-435MS` (url=5076ms, status=HTTP 204)
19. `AKUN-032-INTERNETWORKS-45-131-4-0-VLESS-WS-533MS` (url=776ms, status=HTTP 204)
20. `AKUN-034-CLOUDFLARE-VLESS-WS-510MS` (url=839ms, status=HTTP 204)
21. `AKUN-035-UNKNOWN-VLESS-WS-553MS` (url=928ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
