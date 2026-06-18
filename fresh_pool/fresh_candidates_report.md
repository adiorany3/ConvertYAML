# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 16
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 22

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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-115MS` (url=259ms, nekobox=320ms, status=yes)
2. `AKUN-002-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-116MS` (url=250ms, nekobox=312ms, status=yes)
3. `AKUN-003-RS-RAPIDSEEDBOX-20190717-VLESS-WS-117MS` (url=252ms, nekobox=337ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-129MS`
5. `AKUN-005-CLOUDFLARE-VLESS-WS-130MS`
6. `AKUN-006-RS-RAPIDSEEDBOX-20190717-VLESS-WS-123MS`
7. `AKUN-007-CLOUDFLARE-VLESS-WS-310MS`
8. `AKUN-008-CLOUDFLARE-VLESS-WS-324MS`
9. `AKUN-009-CLOUDFLARE-VLESS-WS-302MS`
10. `AKUN-010-MICROSOFT-VLESS-WS-326MS`
11. `AKUN-014-CLOUDFLARE-VLESS-WS-334MS` (url=716ms, status=HTTP 204)
12. `AKUN-015-CLOUDFLARE-VLESS-WS-328MS` (url=685ms, status=HTTP 204)
13. `AKUN-016-CLOUDFLARE-VLESS-WS-352MS` (url=724ms, status=HTTP 204)
14. `AKUN-021-SPOTIFY-VLESS-WS-506MS` (url=739ms, status=HTTP 204)
15. `AKUN-027-CLOUDFLARE-VLESS-WS-584MS` (url=850ms, status=HTTP 204)
16. `AKUN-035-CLOUDFLARE-VLESS-WS-638MS` (url=1067ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
