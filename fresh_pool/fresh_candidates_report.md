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
1. `AKUN-001-UNKNOWN-VLESS-WS-122MS` (url=280ms, nekobox=281ms, status=yes)
2. `AKUN-002-OVH-VLESS-WS-113MS` (url=246ms, nekobox=287ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-138MS` (url=252ms, nekobox=285ms, status=yes)
4. `AKUN-004-LEVIKOGJGFDD-VLESS-WS-118MS`
5. `AKUN-005-CLOUDFLARE-VLESS-WS-153MS`
6. `AKUN-006-CLOUDFLARE-VLESS-WS-159MS`
7. `AKUN-007-CLOUDFLARE-VLESS-WS-117MS`
8. `AKUN-008-UNKNOWN-VLESS-WS-184MS`
9. `AKUN-009-CLOUDFLARE-VLESS-WS-160MS`
10. `AKUN-010-CLOUDFLARE-VLESS-WS-181MS`
11. `AKUN-014-CLOUDFLARE-VLESS-WS-203MS` (url=278ms, status=HTTP 204)
12. `AKUN-015-CLOUDFLARE-VLESS-WS-137MS` (url=263ms, status=HTTP 204)
13. `AKUN-016-SKK-VLESS-WS-172MS` (url=304ms, status=HTTP 204)
14. `AKUN-017-CLOUDFLARE-VLESS-WS-400MS` (url=876ms, status=HTTP 204)
15. `AKUN-020-CLOUDFLARE-VLESS-WS-424MS` (url=2199ms, status=HTTP 204)
16. `AKUN-028-CLOUDFLARE-VLESS-WS-778MS` (url=1196ms, status=HTTP 204)
17. `AKUN-030-HOSTES-LLC-VLESS-WS-746MS` (url=1187ms, status=HTTP 204)
18. `AKUN-034-CLOUDFLARE-VLESS-WS-863MS` (url=2354ms, status=HTTP 204)
19. `AKUN-035-CLOUDFLARE-VLESS-WS-871MS` (url=1670ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
