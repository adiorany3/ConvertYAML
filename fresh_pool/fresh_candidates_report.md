# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 17
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 21

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
1. `AKUN-001-LEVIKOGJGFDD-VLESS-WS-94MS` (url=294ms, nekobox=337ms, status=yes)
2. `AKUN-002-ZVC-VLESS-WS-115MS` (url=346ms, nekobox=333ms, status=yes)
3. `AKUN-003-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-111MS` (url=1995ms, nekobox=335ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-113MS`
5. `AKUN-005-LEVIKOGJGFDD-VLESS-WS-177MS`
6. `AKUN-006-UNKNOWN-VLESS-WS-110MS`
7. `AKUN-009-CLOUDFLARE-VLESS-WS-100MS` (url=666ms, nekobox=679ms, status=no)
8. `AKUN-007-CLOUDFLARE-VLESS-WS-124MS`
9. `AKUN-008-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-110MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-111MS`
11. `AKUN-013-UNKNOWN-VLESS-WS-502MS` (url=754ms, nekobox=623ms, status=no)
12. `AKUN-014-CLOUDFLARE-VLESS-WS-546MS` (url=1005ms, nekobox=207ms, status=no)
13. `AKUN-010-CLOUDFLARE-VLESS-WS-525MS`
14. `AKUN-017-UNKNOWN-VLESS-WS-576MS` (url=1611ms, status=HTTP 204)
15. `AKUN-025-CLOUDFLARE-VLESS-WS-553MS` (url=830ms, status=HTTP 204)
16. `AKUN-028-CLOUDFLARE-VLESS-WS-574MS` (url=948ms, status=HTTP 204)
17. `AKUN-031-UNKNOWN-VLESS-WS-860MS` (url=4181ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
