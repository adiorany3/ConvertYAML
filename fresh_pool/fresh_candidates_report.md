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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-65MS` (url=207ms, nekobox=239ms, status=yes)
2. `AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-68MS` (url=208ms, nekobox=245ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-77MS` (url=227ms, nekobox=225ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-67MS` (url=214ms, nekobox=255ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-78MS` (url=225ms, nekobox=225ms, status=yes)
6. `AKUN-006-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-93MS` (url=202ms, nekobox=236ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-138MS`
8. `AKUN-008-CLOUDFLARE-VLESS-WS-113MS`
9. `AKUN-009-CLOUDFLARE-VLESS-WS-259MS`
10. `AKUN-010-UNKNOWN-VLESS-WS-261MS`
11. `AKUN-013-CLOUDFLARE-VLESS-WS-266MS` (url=556ms, status=HTTP 204)
12. `AKUN-014-CLOUDFLARE-VLESS-WS-268MS` (url=551ms, status=HTTP 204)
13. `AKUN-015-UNKNOWN-VLESS-WS-213MS` (url=2129ms, status=HTTP 204)
14. `AKUN-016-UNKNOWN-VLESS-WS-235MS` (url=3683ms, status=HTTP 204)
15. `AKUN-018-UNKNOWN-VLESS-WS-382MS` (url=929ms, status=HTTP 204)
16. `AKUN-020-UNKNOWN-VLESS-WS-378MS` (url=823ms, status=HTTP 204)
17. `AKUN-027-UNKNOWN-VLESS-WS-460MS` (url=727ms, status=HTTP 204)
18. `AKUN-031-UNKNOWN-VLESS-WS-518MS` (url=1431ms, status=HTTP 204)
19. `AKUN-032-UNKNOWN-VLESS-WS-599MS` (url=1206ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
