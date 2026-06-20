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
1. `AKUN-001-VULTR-VLESS-WS-133MS` (url=251ms, nekobox=305ms, status=yes)
2. `AKUN-002-ALIBABA-VLESS-WS-127MS` (url=270ms, nekobox=304ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-146MS` (url=281ms, nekobox=294ms, status=yes)
4. `AKUN-004-GOV-VLESS-WS-151MS` (url=262ms, nekobox=300ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-146MS` (url=298ms, nekobox=306ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-157MS` (url=271ms, nekobox=309ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-149MS` (url=274ms, nekobox=318ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-136MS` (url=266ms, nekobox=300ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-148MS` (url=278ms, nekobox=379ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-363MS` (url=700ms, nekobox=731ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-358MS` (url=690ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-374MS` (url=748ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-391MS` (url=752ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-385MS` (url=726ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-405MS` (url=776ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-407MS` (url=787ms, status=HTTP 204)
17. `AKUN-031-UNKNOWN-VLESS-WS-310MS` (url=812ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
